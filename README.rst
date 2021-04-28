#########################
Tapis V2 Actors Templates
#########################

A cookiecutter repository with project templates for Tapis V2 Actors. This repository provides the essential files required to build a Tapis V2 Actor. 
It enables a user to easily start working by modifying a preexisting template for an actor project.

To get started with creating an actor, running the ``tapis actors init`` command will fetch a very simple code skeleton you can fill in and deploy.

cookiecutters is a command-line utility that creates projects from cookiecutters (project templates), e.g. creating a Python package project from a Python package project template. 


###########
Get Started 
###########

-------------------------
Installation of Tapis-CLI 
-------------------------

Documentation: `https://tapis-cli.readthedocs.io/en/latest/ <https://tapis-cli.readthedocs.io/en/latest/>`_


.. code-block:: shell

    $ git clone https://github.com/TACC-Cloud/tapis-cli.git
    $ cd tapis-cli
    $ pip install --upgrade --user .


With Tapis-CLI installed, we can use **cc-tapis-v2-actors**

1. Create a default actor project 

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

2. List the existing cookiecutter actor templates 

.. code-block:: shell

    $ tapis actors init --list-templates
    +-----------+-----------+------------------------------------------------------------+----------+
    | id        | name      | description                                                | level    |
    +-----------+-----------+------------------------------------------------------------+----------+
    | default   | Default   | Basic code and configuration skeleton                      | beginner |
    | echo      | Echo      | Echo input message                                         | beginner |
    | sd2e_base | sd2e_base | Default reactor context for docker://sd2e/reactors:python3 | beginner |
    +-----------+-----------+------------------------------------------------------------+----------+

3. Create a specific existing project from a cookiecutter template 

.. code-block:: shell

    $ tapis actors init --template echo
    +-------+----------------------------------------------+
    | stage | message                                      |
    +-------+----------------------------------------------+
    | setup | Project path: ./echo                         |
    | setup | CookieCutter variable name=echo              |
    | setup | CookieCutter variable project_slug=echo      |
    | setup | CookieCutter variable docker_namespace=reshg |
    | setup | CookieCutter variable docker_registry=e      |
    | clone | Project path: ./echo                         |
    +-------+----------------------------------------------+
 
 
#################
How To Contribute
#################

New actor templates are always welcome ! 

If you have new actor templates to contribute, please follow the steps below:

- Create a pull request to the **main** branch with the new features. 
- The pull request will be reviewed and merged by the maintainer of this repository. 
- Once a new template is added, it will be added to **catalog.json** to update the list of existing templates. 
