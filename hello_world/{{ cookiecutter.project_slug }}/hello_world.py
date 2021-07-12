from agavepy.actors import get_context


# function to say hello world
def say_hello_world(m):
    if not m:
        print("Hello, World!")
    else:
        print(m)

def main():
    context = get_context()
    print(context)
    message = context['raw_message']
    say_hello_world(message)

if __name__ == '__main__':
    main()
