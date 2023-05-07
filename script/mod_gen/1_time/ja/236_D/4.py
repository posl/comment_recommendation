def read():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    return N, A

if __name__ == '__main__':
    read()