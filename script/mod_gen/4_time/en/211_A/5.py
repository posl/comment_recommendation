def main():
    # To read from STDIN
    import sys
    # To read from a file
    #import os
    #filename = os.path.join(os.path.dirname(__file__), 'input.txt')
    #sys.stdin = open(filename, 'r')
    # To write to a file
    #filename = os.path.join(os.path.dirname(__file__), 'output.txt')
    #sys.stdout = open(filename, 'w')
    A, B = map(int, sys.stdin.readline().split())
    C = ((A-B)/(3)) +B
    print(C)

if __name__ == '__main__':
    main()