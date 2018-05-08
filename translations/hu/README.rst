micorbit:Slovensko webstránka
#############################

.. image:: https://d322cqt584bo4o.cloudfront.net/microbitsk-website/localized.svg

`Switch README.rst to English <https://github.com/microbitsk/microbit.sk-website/blob/master/translations/en/README.rst>`_

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
- ``docs`` - Vygenerovaná statická `webová stranka microbit:Slovensko <https://www.microbit.sk>`_. **Neditujte súbory v tomto adresáry, lebo budú pregenerované!** Postup na vygenerovanie je popísany nižšie.


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

- Nainštalujeme závislosti::

    pip install -r requirements.txt

- Spustíme Flask server a prípadne otvoríme vo webovom prehliadači (http://127.0.0.1:5000)::

    python views.py


Pokiaľ nájdete chyby, prosím nahláste ich! Vytvorte prosím `issue na GitHube <https://github.com/microbitsk/microbit.sk-website/issues?template=Bug_report.md>`_. Ak máte nápad na zlepšenie, môžete vytvoriť `issue na GitHube <https://github.com/microbitsk/microbit.sk-website/issues?template=Feature_request.md>`_, prípadne nás navštívte na našom `verejnom chate <https://riot.python.sk/#/room/#general:python.sk>`_, alebo nám napíšte email: `info@microbit.sk <mailto:info@microbit.sk>`_.


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
