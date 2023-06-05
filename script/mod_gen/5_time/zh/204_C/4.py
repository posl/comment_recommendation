def get_input():
    n,m = map(int,input().split())
    ab = []
    for i in range(m):
        ab.append(list(map(int,input().split())))
    return n,m,ab

if __name__ == '__main__':
    get_input()