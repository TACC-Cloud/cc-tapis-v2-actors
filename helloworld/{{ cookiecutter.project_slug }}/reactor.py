import os

from reactors.runtime import Reactor
from reactors.version import version as reactors_version

def main():
    
    r = Reactor()

    # validate the message and context against schemas
    try:
        r.validate_message(permissive=False)
    except Exception as err:
        extype, value, tb = sys.exc_info()
        traceback.print_exc()
        pdb.post_mortem(tb)
        raise

    r.logger.info("Actor received message: {}".format(r.context['raw_message']))
    r.logger.debug("This is a DEBUG message from actor {}".format(r.uid))


if __name__ == '__main__':
    main()
