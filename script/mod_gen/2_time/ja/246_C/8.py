def get_input():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    return n, k, x, a

if __name__ == '__main__':
    get_input()