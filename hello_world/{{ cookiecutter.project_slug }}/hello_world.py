"""
say Hello, World or the message received from user input

:authors: Shweta Gopaulakrishnan (sgopal@tacc.utexas.edu)
"""

from agavepy.actors import get_context


def say_hello_world(m):
    """Print message from user if present, else echo "Hello, World"""
    # if user input is an empty message
    if not m:
        print("Hello, World")
    # print the user input message
    else:
        print(m)


def main():
    """Main entry to grab message context from user input"""
    context = get_context()
    print(context)
    message = context['raw_message']
    say_hello_world(message)

if __name__ == '__main__':
    main()
