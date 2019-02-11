twitter tools
=============

by `Pedro Ivan Lopez <http://pedroivanlopez.com>`_.

Manage friends
--------------

Twitter calls an account you follow *friend*.

Create data directory

::

  mkdir data

Set up your tokens and secrets in the `auth.json` file

Run make to see the targets

::

  make

Select random friends
~~~~~~~~~~~~~~~~~~~~~

Retrieve 10 random following accounts and print in format
``https://twitter.com/<username>/followers_you_follow`` to stdout.

::

  python3 select_random.py
