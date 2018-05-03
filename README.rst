micorbit:Slovensko webstránka
#############################

`Webová stranka microbit:Slovensko <https://www.microbit.sk>`_, založená na frameworku `Flask <http://flask.pocoo.org/>`_, z ktorého sa vygeneruje statické HTML.


Ako pomôct?
-----------

Od komunity pre komunitu. Stránka je spravovaná dobrovoľníkmi a budeme veľmi radi keď sa pridáš. Príspevky su viac než vítané. Prečítaj si našu `prispievateľskú príručku <https://github.com/microbitsk/microbit.sk-website/blob/master/CONTRIBUTING.rst>`_ a pridaj sa k nám!


Štruktúra projektu
------------------

**1 branch**:

- ``master`` - Flask aplikácia, šablony, statické súbory.

**Adresare**

- ``root`` - Flask aplikácia je koreňovom adresáry.
- ``docs`` - Vygenerovaná statická `webová stranka microbit:Slovensko <https://www.microbit.sk>`_. Neditujte súbory v tomto adresáry, lebo budú pregenerované! Postup na vygenerovanie je popísany nižšie.


Inštalácia
----------

Pre vývoj používame Python 3. Príkazy su pre terminál v Linuxe, ale mali by fungovať aj pre Mac OS.

- Naklonujeme si repozitár lokálne ku sebe::

    git clone https://github.com/microbitsk/microbit.sk-website
    cd microbit.sk-website

- Vytvoríme si Python virtualné prostredie (modul venv je súčasť Python 3) a nainštalujeme všetky potrebné závislosti::

    python3 -m venv envs3

- Aktivujeme Python virtuálne prostredie::

    source envs3/bin/activate

- Nainsštalujeme závislosti::

    pip install -r requirements.txt

- Spustíme Flask server a prípadne otvoríme vo webovom prehliadači (http://127.0.0.1:5000)::

    python views.py


Pokiaľ nájdete chyby, prosím nahláste ich! Vytvorte prosím issue na GitHube. Ak máte nápad na zlepšenie, môžete vytvoriť issue na GitHube, prípadne nás navštívte na našom verejnom chate
`<https://riot.python.sk/#/room/#general:python.sk>`_, alebo nám napíšte email: `info@microbit.sk <mailto:info@microbit.sk>`_.


Webové odkazy
-------------

- web: `https://www.microbit.sk <https://www.microbit.sk/>`_, `https://www.micropython.sk <https://www.micropython.sk/>`_, `https://www.python.sk <https://www.python.sk/>`_
- chat: `https://riot.python.sk <https://riot.python.sk/#/room/#general:python.sk>`_
- email: `info@microbit.sk <mailto:info@microbit.sk>`_

Licencia 
--------

MIT licencia pre kód (GitHub repo), CC-BY pre ostatný obsah (pokiaľ nie je stanovené ináč). Viac informácií o licenciách je v súbore LICENSE.

-----------------

micorbit:Slovakia Website
####################

`micorbit:Slovakia Website <https://www.microbit.sk>`_, built with `Flask <http://flask.pocoo.org/>`_ from which static HTML is generated.


Contributing
------------

From community to the community. Contributions are welcome. Read our `contribution guide <https://github.com/microbitsk/microbit.sk-website/blob/master/CONTRIBUTING.rst>`_ and feel free to join, we would love to hear from you.


Project structure
-----------------

**1 branch**:

- ``master`` - the Flask app, templates, static files.

**Directories**

- ``root`` - Flask app is in root directory.
- ``docs`` - Generated static `website microbit:Slovakia <https://www.microbit.sk>`_. Do not edit files in this directory, they will be regenerated! Read below how to generate.


Installation
------------

We use Python 3 for development. Commands are made for terminal in Linux, and should work in Mac OS.

- clone repository locally::

    git clone https://github.com/microbitsk/microbit.sk-website
    cd microbit.sk-website

- creates a virtual environment (module venv is part of Python 3) and installs all requirements::

    python3 -m venv envs3

- activate virtual environments::

    source envs3/bin/activate

- install requirements::

    pip install -r requirements.txt

- start flask server, and you can view it in browser (http://127.0.0.1:5000)::

    python views.py


If you find some bug please do report it! Create issue at our GitHub. Feel free to submit suggestions vie GitHub issues as well, or join us in our `public chat <https://riot.python.sk/#/room/#general:python.sk>`_ or send us an email: `info@microbit.sk <mailto:info@microbit.sk>`_.


Links
-----

- web: `https://www.microbit.sk <https://www.microbit.sk/>`_, `https://www.micropython.sk <https://www.micropython.sk/>`_, `https://www.python.sk <https://www.python.sk/>`_
- chat: `https://riot.python.sk <https://riot.python.sk/#/room/#general:python.sk>`_
- email: `info@microbit.sk <mailto:info@microbit.sk>`_


License
-------

MIT license for code (GitHub repo), CC-BY for content (if not stated otherwise). For more detail read the LICENSE file.

