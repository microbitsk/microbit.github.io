Contributors Guide
==================

We are happy with any volunteers involvement in `microbit.sk <https://www.microbit.sk>`_ website. If you would like to help us, there are multiple ways to do so. Depending on your skills and type of work you would like to do (doesn’t have to be development), we encourage you to start with any of the following:

Write a blog, get involved on social media or make a talk
--------------------------------------------------------------------

You can help out by spreading the word about `microbit.sk <https://github.com/microbitsk/microbit.sk-website>`_, or joining `public chat <https://riot.python.sk/#/room/#general:python.sk>`_ (if there is Slovak chatter, don't worry just start in English) to help others or share your ideas and experiences with people in the community. Alternatively reach us via email: `info@microbit.sk <mailto:info@microbit.sk>`_.

Update documentation
-----------------------

`GitHub wiki <https://github.com/pyconsk/www.python.sk/wiki>`_ is used to guide people
and developers the right way. **Currently it is empty and we have to start somehow...** If you don't know how to do something,
we probably missed it in our wiki. Documentation is a never ending process so we welcome
any improvement suggestions, feel free to create issues in our bug tracker.

If you feel that our documentation needs to be modified or we missed something,
feel free to submit PR, or get in touch with us at our `public chat <https://riot.python.sk/#/room/#general:python.sk>`_ (if there is Slovak chatter, don't worry just start in English).

Suggest an improvement or report bug
--------------------------------------

All issues are handled by `Github issue tracker <https://github.com/microbitsk/microbit.sk-website/issues>`_, if you've found a bug please create an issue for it.

If there is something you are missing, and wish to be implemented in `Github issue tracker <https://github.com/microbitsk/microbit.sk-website/issues>`_, feel free to create an issue and mark it as an enhancement.

Update microbit.sk
----------------------

All development is done on `Github <https://github.com/microbitsk/microbit.sk-website>`_. If you decide to work on existing issue, **please mention in the issue comment that you are working on it so other people do not work on the same issue**. Create your `fork <https://github.com/microbitsk/microbit.sk-website/fork>`_ and **in new branch update code**.
Once you are happy with your changes create `pull request <https://help.github.com/articles/using-pull-requests>`_ and we will review and merge it as soon as we can.
To make the life easier please do all your work in a `separate branch <https://git-scm.com/book/en/v1/Git-Branching>`_ (if there are multiple commits we do `squash merge <https://github.com/blog/2141-squash-your-commits>`_), if there is an issue for your change
should include the issue number in the branch name and merge request description so they are linked on GitHub.

Getting help
---------------

If you look for help, visit our `monthly meetups in Bratislava <https://pycon.sk/sk/meetup.html>`_ or give us a shout at `public chat <https://riot.python.sk/#/room/#general:python.sk>`_ (if there is Slovak chatter, don't worry just start in English). Alternatively, reach us via email: `info@microbit.sk <mailto:info@microbit.sk>`_.

Developer's HowTo
=====================

Development standards
----------------

* We do use standard PEP8, with an extended line to 119 characters.

Development setup
--------------------------------

This is standard Flask app. Follow steps in (in Linux, or Mac):

1. ``git clone git@github.com:YOUR-GITHUB-ACCOUNT/microbit.sk-website.git`` make a clone of your fork of microbit.sk-website
2. ``cd microbit.sk-website`` lets go inside the project directory
3. ``python3 -m venv envs3`` this will create virtual environments for you, where you can install all requirements needed
4. ``source envs3/bin/activate`` activate virtual environments
5. ``pip install -r doc/requirements.txt`` install out main dependency
6. ``python views.py`` start development server, and check the app in browser

Development methodology
---------------

1. You create a `fork <https://github.com/microbitsk/microbit.sk-website/fork>`_ of the project (you do this only once. Afterward, you already have it in your GitHub, it is your repo in which you are doing all the development).
2. Clone your fork locally ``git clone git@github.com:YOUR-GITHUB-ACCOUNT/microbit.sk-website.git`` add upstream remote to be able to download updated into your fork ``git remote add upstream https://github.com/microbitsk/microbit.sk-website.git``. You don't have the right to push to upstream, but do regularly pull and push to your fork to keep it up-to-date and prevent conflicts.
3. Pick up a `issue <https://github.com/microbitsk/microbit.sk-website/issues>`_, and make a comment that you are working on it.
4. In your local git copy, you create a branch: ``git checkout -b XX-new-feature`` (where XX is issue number).
5. Coding time:

   * Do commit how often you need. At this point doesn't matter if the code is broken between commits.
   * Ulož svoju zmenu vo svojom repozitári na GitHube. Na server môžeš pushnúť svoj kód koľkokrát len chceš: ``git push origin XX-nova-funkcia``.
   * Merguj kód z upstreamu, kedykoľvek chceš: ``git pull upstream master``. Tu nás nezaujímajú správy o mergovaní, prípadne použi rebase, aby si sa ich zbavil. Nakoniec urobíme `squash merge <https://github.com/blog/2141-squash-your-commits>`_ (v hlavnej vetve na upstreame to bude vyzerať ako jeden commit).

6. Keď si so svojím kódom spokojný/á, klikni na tlačítko `pull request <https://help.github.com/articles/using-pull-requests>`_ a vyber si z upstreamu vetvu master a XX-nova-funkcia zo svojho repozitára. Potom sa spustia automatické testy, ktoré overia, či je všetko OK. Ak uvidíš nejké chyby, oprav ich a pushni opravu do svojej vetvy. Takto sa pull request zaktualizuje o opravy a testy sa spustia znova.
7. Ak niekto kontroluje tvoj kód a požiada ťa o zmenu, môžeš postupovať podľa bodu 5. Ak si so zmenami hotový/á, urob do pull requestu poznámku, aby sa mohla opäť urobiť revízia.
8. Tvoja funkcionalita je schválená a zmergovaná do mastra v upstreame, takže si môžeš otvorit vetvu master vo svojej lokálnej kópii: ``git checkout master`` a stiahnuť si novo schválené zmeny z upstreamu ``git pull upstream master``. Stiahnutie z upstreamu stiahne tvoju prácu (ako jeden commit do mastra) ktorú si urobil/a v samostatnej vetve. Teraz môžeš zmazať svoju lokálnu vetvu ``git branch --delete XX-nova-funkcia`` a aj vzdialenú ``git push origin :XX-nova-funkcia``

Zdá sa ti to príliš zložité? Netráp sa tým, keď budeš postupovať podľa vyššie uvedených krokov, uvidíš, že si na to ľahko zvykneš. Okrem toho, podobný postup sa používa v takmer každom väčšom open source projekte a podobne to chodí aj v korporátnom prostredí. Ak si nevieš rady, neváhaj a poď na náš `verejný chat <https://riot.python.sk/#/room/#general:python.sk>`_ a požiadaj o pomoc. Kontaktovať nás môžeš aj emailom: `info@microbit.sk <mailto:info@microbit.sk>`_.
