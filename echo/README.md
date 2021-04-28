
**Echo actor**

This is a cookiecutter template for an "echo" actor.
This is an Actor to echo the input message. 

The template can be used with Tapis CLI tapis-cli as follows:

tapis actors init --template echo
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

This would create a subfolder echo/ with the required files.
