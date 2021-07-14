#########################
Tapis V2 Actors Templates
#########################

A `cookiecutter <https://github.com/cookiecutter/cookiecutter>`_ repository with project templates for Tapis V2 Actors. This repository provides the essential files required to build a Tapis V2 Actor.
It enables a user to easily start working by modifying a preexisting template for an actor project.

cookiecutters is a command-line utility that creates projects from cookiecutters (project templates), e.g. creating a Python package project from a Python package project template.


###########
Get Started
###########

This repository is consumed by `Tapis-CLI <https://tapis-cli.readthedocs.io/en/latest/>`_.
To get started with creating an actor, running the ``tapis actors init`` command will fetch a very simple code skeleton you can fill in and deploy.

Let us begin by installing Tapis-CLI.

-------------------------
Installation of Tapis-CLI
-------------------------

The `Tapis-CLI <https://tapis-cli.readthedocs.io/en/latest/>`_ is available as a Python package.

.. code-block:: shell

    $ pip install tapis-cli


With Tapis-CLI **installed and configured**, let us see how we can use our cookiecutter **cc-tapis-v2-actors**.

We can create a default actor with ``tapis actors init`` as shown below.

.. code-block:: shell

    $ tapis actors init
    +-------+----------------------------------------------+
    | stage | message                                      |
    +-------+----------------------------------------------+
    | setup | Project path: ./new_actor                    |
    | setup | CookieCutter variable name=new_actor         |
    | setup | CookieCutter variable project_slug=new_actor |
    | setup | CookieCutter variable docker_namespace=reshg |
    | setup | CookieCutter variable docker_registry=e      |
    | clone | Project path: ./new_actor                    |
    +-------+----------------------------------------------+

Our default actor was pretty cool!
But, we have more than a default template. To check our library of existing templates, run the following command:

.. code-block:: shell

    $ tapis actors init --list-templates
    +--------------------+--------------------+--------------------------------------------------------+----------+
    | id                 | name               | description                                            | level    |
    +--------------------+--------------------+--------------------------------------------------------+----------+
    | default            | Default            | Basic code and configuration skeleton                  | beginner |
    | echo               | Echo               | Echo message                                           | beginner |
    | hello_world        | Hello World        | Say Hello, World!                                      | beginner |
    | sd2e_base          | sd2e_base          | Default reactor context for                            | beginner |
    |                    |                    | docker://sd2e/reactors:python3                         |          |
    | tacc_reactors_base | tacc_reactors_base | Default actor context for                              | beginner |
    |                    |                    | docker://sd2e/reactors:python3                         |          |
    +--------------------+--------------------+--------------------------------------------------------+----------+

To use one of the above templates, we can do the following:

.. code-block:: shell

    $ tapis actors init --template hello_world
    +-------+----------------------------------------------+
    | stage | message                                      |
    +-------+----------------------------------------------+
    | setup | Project path: ./new_actor                    |
    | setup | CookieCutter variable name=echo              |
    | setup | CookieCutter variable project_slug=echo      |
    | setup | CookieCutter variable docker_namespace=reshg |
    | setup | CookieCutter variable docker_registry=e      |
    | clone | Project path: ./new_actor                    |
    +-------+----------------------------------------------+

This would give a new_actor/ project with all the required files to help you create your own actor.
For more information on what the different files do, check our documentation at `Tapis-CLI How-To-Guide <https://tapis-cli-how-to-guide.readthedocs.io/en/latest/actors/create_a_custom_actor.html>`_.

With the new_actor/, let us deploy it.

.. note::
   
   Rename **secrets.jsonsample** to *secrets.json*


.. code-block:: shell

    $ cd new_actor/
    $ tapis actors deploy
    
#################
How To Contribute
#################

New actor templates are always welcome !

If you have a new actor template to contribute, please join our `Slack <http://bit.ly/join-tapis>`_ channel.

Here is what happens when you contribute towards our repository:

* You create a pull request to the **main** branch with the new features.
* We review the pull request and merge it.
* The new template is added to the **catalog.json** to update the list of existing templates.

Hooray, thank you for contributing!
