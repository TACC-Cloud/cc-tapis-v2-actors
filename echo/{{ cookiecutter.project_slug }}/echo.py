"""
echo the message received from user input

:authors: Shweta Gopaulakrishnan (sgopal@tacc.utexas.edu)
"""
from agavepy.actors import get_context


def echo(m):
    """Echo message received from user input."""
    print("Echoing the message: {}".format(m))


def main():
    """Main entry to grab message context from user input"""
    context = get_context()
    message = context['raw_message']
    echo(message)


if __name__ == '__main__':
    main()
