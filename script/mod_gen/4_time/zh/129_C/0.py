def get_input():
    N, M = map(int, input().split())
    a = [0] * (M + 2)
    a[0] = 0
    a[M + 1] = N
    for i in range(1, M + 1):
        a[i] = int(input())
    return N, M, a

if __name__ == '__main__':
    get_input()