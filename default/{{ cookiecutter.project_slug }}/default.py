import os
from agavepy.actors import get_context


def main():
    context = get_context()
    m = context['message_dict']['text']
    print("Actor received message: {}".format(m))

if __name__ == '__main__':
    main()
