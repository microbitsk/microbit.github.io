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


If you find some bug please do report it! Create an issue on our GitHub. Ak máte nápad na zlepšenie, môžete vytvoriť issue na GitHube, prípadne nás navštívte na našom verejnom chate
`<https://riot.python.sk/#/room/#general:python.sk>`_, alebo nám napíšte email: `info@microbit.sk <mailto:info@microbit.sk>`_.


Preklady
--------

Pomôžte nám preložiť stránku do cudzích jazykov. Na preklad nemusíte mať žiadnu znalosť programovania, stačí vedieť iba cudzí jazyk. Preklad zabezpečujeme pomocou služby `crowdin.com <https://crowdin.com/project/microbitsk-website>`_.


Vygenerujeme statickú stránku
-----------------------------

`Frozen-Flask <https://pythonhosted.org/Frozen-Flask/>`_ "zamrzne" Flask aplikáciu do statických súborov. Výsledok môže byť uložený na servery a zobrazovanú iba pomocou klasického web serveru.

- vygenerujeme statickú stránku, výsledok je uložený v ``docs`` adresáry::

    python freezer.py

- preveríme výsledok v prehliladači (http://127.0.0.1:8000/en/index.html)::

    cd docs
    python -m SimpleHTTPServer 8000


Continuous Deployment
---------------------

Všetko čo sa dostane to master vetvy (branch) je automaticky zobrazené na servery. Zobrazuje sa iba vygenerovaná statická stránka ktorá je v ``docs`` adresáry.


Webové odkazy
-------------

- web: `https://www.microbit.sk <https://www.microbit.sk/>`_, `https://www.micropython.sk <https://www.micropython.sk/>`_, `https://www.python.sk <https://www.python.sk/>`_
- chat: `https://riot.python.sk <https://riot.python.sk/#/room/#general:python.sk>`_
- email: `info@microbit.sk <mailto:info@microbit.sk>`_

Licencia 
--------

MIT licencia pre kód (GitHub repo), CC-BY pre ostatný obsah (pokiaľ nie je stanovené ináč). Viac informácií o licenciách je v súbore LICENSE (iba po anglicky).
