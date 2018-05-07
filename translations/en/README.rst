micorbit:Slovakia website
#############################

.. image:: https://d322cqt584bo4o.cloudfront.net/microbitsk-website/localized.svg

`Zobraziť README.rst v Slovenčine <https://github.com/microbitsk/microbit.sk-website/blob/master/README.rst>`_

`micorbit:Slovakia Website <https://www.microbit.sk>`_, built with `Flask <http://flask.pocoo.org/>`_ from which static HTML is generated.

Contributing
------------

From community to the community. Website is managed by volunteers and we'll be happy if you'll join us. Contributions are welcome. Read our `contribution guide <https://github.com/microbitsk/microbit.sk-website/blob/master/CONTRIBUTING_en.rst>`_ and feel free to join, we would love to hear from you!


Project structure
------------------

**1 branch**:

- ``master`` - the Flask app, templates, static files.

**Directories**

- ``root`` - Flask app is in root directory.
- ``docs`` - Generated static `website microbit:Slovakia <https://www.microbit.sk>`_. Do not edit files in this directory, they will be regenerated! Read below how to generate.


Installation
----------

We use Python 3 for development. Commands are made for terminal in Linux, and should work in Mac OS.

- clone repository locally::

    git clone https://github.com/microbitsk/microbit.sk-website
    cd microbit.sk-website

- creates a virtual environment (module venv is part of Python 3) and installs all requirements::

    python3 -m venv envs3

- activate virtual environments::

    source envs3/bin/activate

- Nainsštalujeme závislosti::

    pip install -r requirements.txt

- start flask server, and you can view it in the browser (http://127.0.0.1:5000)::

    python views.py


If you find some bug please do report it! Create an issue on our GitHub. Feel free to submit suggestions via GitHub issues as well, or join us in our public chat
`<https://riot.python.sk/#/room/#general:python.sk>`_ or send us an email: `info@microbit.sk <mailto:info@microbit.sk>`_.


Translations
--------

Help us to translate website in more languages. Na preklad nemusíte mať žiadnu znalosť programovania, stačí vedieť iba cudzí jazyk. Preklad zabezpečujeme pomocou služby `crowdin.com <https://crowdin.com/project/microbitsk-website>`_.


Generate static site
-----------------------------

`Frozen-Flask <https://pythonhosted.org/Frozen-Flask/>`_ freezes a Flask application into a set of static files. The result can be hosted without any server-side software other than a traditional web server.

- generate static files, and you can find them in ``docs`` directory::

    python freezer.py

- verify the generated result in browser (http://127.0.0.1:8000/en/index.html)::

    cd docs
    python -m SimpleHTTPServer 8000


Continuous Deployment
---------------------

Anything committed to master branch ``docs`` directory will be automatically deployed on live server. Live site contain only generated static site in ``docs`` directory.


Links
-------------

- web: `https://www.microbit.sk <https://www.microbit.sk/>`_, `https://www.micropython.sk <https://www.micropython.sk/>`_, `https://www.python.sk <https://www.python.sk/>`_
- chat: `https://riot.python.sk <https://riot.python.sk/#/room/#general:python.sk>`_
- email: `info@microbit.sk <mailto:info@microbit.sk>`_

License 
--------

MIT license for code (GitHub repo), CC-BY for content (if not stated otherwise). For more detail read the LICENSE file.
