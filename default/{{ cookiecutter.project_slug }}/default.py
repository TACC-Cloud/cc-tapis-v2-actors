import os
from agavepy.actors import get_context


def main():
    context = get_context()
    print(context)
    m = context['raw_message']
    print("Actor received message: {}".format(m))

if __name__ == '__main__':
    main()
