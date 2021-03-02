import os

from reactors.runtime import Reactor


def main():

    r = Reactor()
    m = r.context.message_dict
    r.logger.info("message: {}".format(m))


if __name__ == '__main__':
    main()
