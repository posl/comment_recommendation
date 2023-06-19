def get_nut():
    n = int(input())
    nut = list(map(int, input().split()))
    return n, nut

if __name__ == '__main__':
    get_nut()