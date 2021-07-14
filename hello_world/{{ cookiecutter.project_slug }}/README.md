# Hello World

The `"Hello world"` of Tapis Actors SDK. This actor says "Hello, World" or the message passed to it.  

## Quick Start

- Deploy the actor

```
$ tapis actors init --template hello_world
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
```

- Deploy the actor
**Note:** Rename the secrets.jsonsample

```
$ cd new_actor/

$ tapis actors deploy
Building reshg/new_actor:1.0.0
Finished (1490 msec)
Pushing reshg/new_actor:1.0.0
Finished (4605 msec)
+--------+---------------------------------------------------------------------------------------------------+
| stage  | message                                                                                           |
+--------+---------------------------------------------------------------------------------------------------+
| build  | Step 1/5 : FROM python:3.7-alpine                                                                 |
| build  |  ---> 93ac4b41defe                                                                                |
|        |                                                                                                   |
| build  | Step 2/5 : ADD requirements.txt /requirements.txt                                                 |
| build  |  ---> Using cache                                                                                 |
|        |                                                                                                   |
| build  |  ---> 44cc2569e6f4                                                                                |
|        |                                                                                                   |
| build  | Step 3/5 : RUN pip3 install -r /requirements.txt                                                  |
| build  |  ---> Using cache                                                                                 |
|        |                                                                                                   |
| build  |  ---> 46f2739f79c9                                                                                |
|        |                                                                                                   |
| build  | Step 4/5 : ADD hello_world.py /hello_world.py                                                     |
| build  |  ---> Using cache                                                                                 |
|        |                                                                                                   |
| build  |  ---> 983ab4d840ad                                                                                |
|        |                                                                                                   |
| build  | Step 5/5 : CMD ["python", "/hello_world.py"]                                                      |
| build  |  ---> Using cache                                                                                 |
|        |                                                                                                   |
| build  |  ---> 18e4c33229d4                                                                                |
|        |                                                                                                   |
| build  | Successfully built 18e4c33229d4                                                                   |
|        |                                                                                                   |
| build  | Successfully tagged reshg/new_actor:1.0.0                                                         |
|        |                                                                                                   |
| push   | The push refers to repository [docker.io/reshg/new_actor]                                         |
| push   | 1.0.0: digest: sha256:a4340347ac4bfb95173212a9f6470abafd0a5faf4a7ce44e2d85d22700dd763c size: 1994 |
| create | Created Tapis actor JYRL4kZkbz7o                                                                  |
| cache  | Cached actor identifier to disk                                                                   |
+--------+---------------------------------------------------------------------------------------------------+
```

Grab the Actor ID from the above output

- Let's send a message to the actor

```
$ tapis actors submit -m "Hello, World" JYRL4kZkbz7o
+-------------+---------------+
| Field       | Value         |
+-------------+---------------+
| executionId | JBrZwl137JGVv |
| msg         | Hello, World  |
+-------------+---------------+
```

- Monitor the Execution Logs with the Actor ID and Execution ID.

```
$ tapis actors execs logs JYRL4kZkbz7o JBrZwl137JGVv
Logs for execution JBrZwl137JGVv
 Actor received message: Hello, World
```
