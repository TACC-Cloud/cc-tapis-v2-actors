
Echo actor
This is a cookiecutter template for a "default" actor.

The template can be used with Tapis CLI tapis-cli as follows:

tapis actors init --template default
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

This would create a subfolder new_actor/ with the required files.
