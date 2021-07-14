"""
default actor to print the message from user input
"""
from agavepy.actors import get_context


def main():
    """Main entry to grab message context from user input"""
    context = get_context()
    print(context)
    m = context['raw_message']
    print("Actor received message: {}".format(m))


if __name__ == '__main__':
    main()
