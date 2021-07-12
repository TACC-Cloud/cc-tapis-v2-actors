from agavepy.actors import get_context


# function to say hello world
def echo(m):
    print("Echoing the message: {}".format(m))

def main():
    context = get_context()
    print(context)
    message = context['raw_message']
    echo(message)

if __name__ == '__main__':
    main()
