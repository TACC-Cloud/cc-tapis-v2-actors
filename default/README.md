Default actor
=============

This is a cookiecutter template for a "default" actor. 

The template can be used with Tapis CLI `tapis-cli` as follows:

```
tapis actors init --list-templates
+-----------+-----------+-----------------------------------------------------------+----------+
| id        | name      | description                                               | level    |
+-----------+-----------+-----------------------------------------------------------+----------+
| default   | Default   | Basic code and configuration skeleton                     | beginner |
| echo      | Echo      | Echo input message                                        | beginner |
| sd2e_base | sd2e_base | Default reactor context for                               | beginner |
|           |           | docker://sd2e/reactors:python3                            |          |
+-----------+-----------+-----------------------------------------------------------+----------+

tapis actors init --template default 
``` 

This would create a subfolder default/ with the required files. 

