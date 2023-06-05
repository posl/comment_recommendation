def get_input():
    N, M = map(int, input().split())
    for i in range(M):
        a, b = map(int, input().split())
        yield a, b

if __name__ == '__main__':
    get_input()