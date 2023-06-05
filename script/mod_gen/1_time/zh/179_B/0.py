def get_input():
    n = int(input())
    d = []
    for i in range(n):
        d.append(list(map(int, input().split())))
    return n, d

if __name__ == '__main__':
    get_input()