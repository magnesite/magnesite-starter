import builtins, sys, os

def open(path):
    f = builtins.open(path, 'r')
    return UpperCaser(f)



if __name__ == '__main__':
    print('hi')