def main():
    import sys
    import math
    import re
    def get_list():
        return list(map(int, sys.stdin.readline().strip().split()))
    def get_int():
        return int(sys.stdin.readline().strip())
    def get_str():
        return sys.stdin.readline().strip()
    def get_list_str():
        return list(sys.stdin.readline().strip())
    R, X, Y = get_list()
    if (X**2 + Y**2)**(1/2) < R:
        print(2)
    else:
        print(math.ceil((X**2 + Y**2)**(1/2)/R))

if __name__ == '__main__':
    main()