def get_input():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    return n, q, a, x

if __name__ == '__main__':
    get_input()