def get_input():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    return n, x, y, z, a, b

if __name__ == '__main__':
    get_input()