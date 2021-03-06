

It is recommended to first install `pyenv <https://github.com/pyenv/pyenv>`_,
then `pipsi <https://github.com/mitsuhiko/pipsi>`_.  
Then simply install `pew <https://github.com/berdario/pew>`_ and
`pipenv <https://github.com/pypa/pipenv>`_ with pipsi.

pipsi installs scripts (system wide available) provided by Python packages
into separate virtualenvs to shield them from your system and each other.

As a command line tool
---------------------------------

.. code:: bash

    $ pipsi install --python=python2.7 .
    ✨🍰✨

    $ ticket-tools-avalanche --help
    Usage: ticket-tools-avalanche [OPTIONS]

    Options:
        --incidentid INTEGER  ID of incident.
        --tplname TEXT        Name of the template
        --csv TEXT            List of IPs
        --help                Show this message and exit.



As a library
---------------

.. code:: bash

    $ pipenv install .
    ✨🐍✨
