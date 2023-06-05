def get_input():
    n = int(input())
    tlr = []
    for _ in range(n):
        tlr.append(list(map(int,input().split())))
    return n,tlr

if __name__ == '__main__':
    get_input()