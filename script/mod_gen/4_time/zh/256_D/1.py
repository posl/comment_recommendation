def get_input():
    N = int(input())
    l = []
    for i in range(N):
        l.append(list(map(int, input().split())))
    return N, l

if __name__ == '__main__':
    get_input()