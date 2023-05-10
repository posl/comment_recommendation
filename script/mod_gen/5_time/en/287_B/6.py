def get_input():
    n,m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    return n,m,s,t

if __name__ == '__main__':
    get_input()