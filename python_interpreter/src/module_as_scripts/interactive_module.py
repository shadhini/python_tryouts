import sys


def interactive_module_function(arg):
    print(f"The argument is: {arg}")


if __name__ == '__main__':
    args = sys.argv

    interactive_module_function(args[1])
