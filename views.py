#!/usr/bin/python
# -*- coding: utf8 -*-
import os
from datetime import datetime
from flask import Flask, g, request, render_template, abort, make_response
from flask_babel import Babel, gettext

app = Flask(__name__, static_url_path='/static')
app.config['BABEL_DEFAULT_LOCALE'] = 'sk'
app.config['FREEZER_DESTINATION'] = 'docs'
app.jinja_options = {'extensions': ['jinja2.ext.with_', 'jinja2.ext.i18n']}
babel = Babel(app)

CNAME = 'microbit.sk'
SRC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))
LOGO_PYCON = 'logo/pycon.svg'

# LANGS = ('sk', 'en', 'de', 'hu', 'cs', 'ru')
LANGS = ('sk', 'en')

TIME_FORMAT = '%Y-%m-%dT%H:%M:%S+00:00'
NOW = datetime.utcnow().strftime(TIME_FORMAT)


def get_mtime(filename):
    mtime = datetime.fromtimestamp(os.path.getmtime(filename))
    return mtime.strftime(TIME_FORMAT)


SITEMAP_DEFAULT = {'prio': '0.1', 'freq': 'weekly'}
SITEMAP = {
    'sitemap.xml': {'prio': '0.9', 'freq': 'daily', 'lastmod': get_mtime(__file__)},
    'index.html': {'prio': '1', 'freq': 'daily'},
}
LDJSON = {
    "@context": "http://schema.org",
    "@type": "Organization",
    "name": "SPy o.z.",
    "url": "https://"+ CNAME,
    "logo": "https://"+ CNAME +"/static/img/logo/python.svg",
    "sameAs": [
        "https://facebook.com/pyconsk",
        "https://twitter.com/pyconsk",
        "https://www.linkedin.com/company/spy-o--z-",
        "https://github.com/pyconsk",
    ]
}


@app.before_request
def before():
    if request.view_args and 'lang_code' in request.view_args:
        g.current_lang = request.view_args['lang_code']
        request.view_args.pop('lang_code')


@babel.localeselector
def get_locale():
    # try to guess the language from the user accept
    # header the browser transmits. The best match wins.
    # return request.accept_languages.best_match(['de', 'sk', 'en'])
    return g.get('current_lang', app.config['BABEL_DEFAULT_LOCALE'])


def _get_template_variables(**kwargs):
    variables = {
        'title': gettext('microbit.sk'),
        'logo': LOGO_PYCON,
        'ld_json': LDJSON,
        'langs': LANGS,
        'CNAME': CNAME,
    }
    variables.update(kwargs)

    if 'current_lang' in g:
        variables['lang_code'] = g.current_lang

        if g.current_lang not in LANGS:
            return abort(404)
    else:
        variables['lang_code'] = app.config['BABEL_DEFAULT_LOCALE']

    return variables


def redirect():
    template_variables = _get_template_variables(li_index='active')
    template_variables['redirect_url'] = 'https://ucimeshardverom.sk'

    return render_template('redirect.html', **template_variables)

@app.route('/')
def landing_page():
    template_variables = _get_template_variables(li_index='active')

    return render_template('index.html', **template_variables)

@app.route('/index.html')
def landing_index():
    template_variables = _get_template_variables(li_index='active')

    return render_template('index.html', **template_variables)

@app.route('/CNAME')
def gh_cname():
    return CNAME

@app.route('/<lang_code>/index.html')
def index():
    template_variables = _get_template_variables(li_index='active')

    return render_template('index.html', **template_variables)

@app.route('/<lang_code>/old.html')
def old():
    template_variables = _get_template_variables(li_index='active')

    return render_template('old/index.html', **template_variables)

def get_lastmod(route, sitemap_entry):
    """Used by sitemap() below"""
    if 'lastmod' in sitemap_entry:
        return sitemap_entry['lastmod']

    template = route.rule.split('/')[-1]
    template_file = os.path.join(SRC_DIR, 'templates', template)

    if os.path.exists(template_file):
        return get_mtime(template_file)

    return NOW


@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    """Generate sitemap.xml. Makes a list of urls and date modified."""
    domain = 'https://'+ CNAME
    pages = []

    # static pages
    for rule in app.url_map.iter_rules():

        if "GET" not in rule.methods:
            raise Exception

        if 'lang_code' in rule.arguments:
            indx = rule.rule.replace('/<lang_code>/', '')

            for lang in LANGS:
                alternate = []

                for alt_lang in LANGS:
                    if alt_lang != lang:
                        alternate.append({
                            'lang': alt_lang,
                            'url': domain + rule.rule.replace('<lang_code>', alt_lang).replace('index.html', '')
                        })

                sitemap_data = SITEMAP.get(indx, SITEMAP_DEFAULT)
                pages.append({
                    'loc': domain + rule.rule.replace('<lang_code>', lang).replace('index.html', ''),
                    'alternate': alternate,
                    'lastmod': get_lastmod(rule, sitemap_data),
                    'freq': sitemap_data['freq'],
                    'prio': sitemap_data['prio'],
                })
        elif rule.rule == '/sitemap.xml':
            indx = rule.rule.replace('/', '')
            sitemap_data = SITEMAP.get(indx, SITEMAP_DEFAULT)
            pages.append({
                'loc': domain + rule.rule,
                'lastmod': get_lastmod(rule, sitemap_data),
                'freq': sitemap_data['freq'],
                'prio': sitemap_data['prio'],
            })

    sitemap_xml = render_template('sitemap_template.xml', pages=pages)
    response = make_response(sitemap_xml)
    response.headers["Content-Type"] = "text/xml"

    return response


if __name__ == "__main__":
    app.run(debug=True, host=os.environ.get('FLASK_HOST', '127.0.0.1'), port=int(os.environ.get('FLASK_PORT', 5000)))
