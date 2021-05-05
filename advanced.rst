##################
Using Cookiecutter
##################

cookiecutters is a command-line utility that creates projects from cookiecutters (project templates), e.g. creating a Python package project from a Python package project template.

To use cc-tapis-v2-actors with cookiecutter:

.. code-block:: shell

   $ cookiecutter https://github.com/TACC-Cloud/cc-tapis-v2-actors.git
   This would create a .cookiecutters/cc-tapis-v2-actors directory.

   $ cd .cookiecutters/cc-tapis-v2-actors
   Use a template to create a new actor project.
   $ cookiecutter default
   > Enter the prompt values to populate the cookiecutter.json.
     name [reactor]: word_count_actor
     token [True]:
     description [Short description of the reactor]: A simple word count actor that counts and prints the number of words in a provided message.
     version [0.0.1]:
     alias: word_count_actor
     reactor_stateless [True]:
     dockerfile [Dockerfile]:
     docker_namespace []: <Docker Hub username>
     docker_base_repo [python:3.7-alpine]:
     docker_hub_org []:
     project_slug [reactor]:

This would create a project folder word-count-actor/ with the following tree:

.. code-block:: bash

   $ tree ../word-count-actor/
   word-count-actor/
   ├── Dockerfile
   ├── project.ini
   ├── config.yml
   ├── default.py
   ├── requirements.txt
   ├── secrets.jsonsample
   └── message.jsonschema

This is a very simple code skeleton you can fill in and deploy.
For more information on what the different files do, check our documentation at `Tapis-CLI How-To-Guide <https://tapis-cli-how-to-guide.readthedocs.io/en/latest/actors/create_a_custom_actor.html>`_
