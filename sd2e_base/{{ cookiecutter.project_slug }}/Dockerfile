FROM {{ cookiecutter.docker_base_repo }}

# add reactor assets
ADD requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt 
ADD reactor.py /
ADD config.yml /
ADD context_schemas /
ADD message_schemas /