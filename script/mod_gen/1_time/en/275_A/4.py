def get_input():
    n = int(input())
    heights = [int(x) for x in input().split()]
    return n, heights

if __name__ == '__main__':
    get_input()