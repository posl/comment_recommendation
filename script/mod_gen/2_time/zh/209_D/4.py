def get_input():
    N,Q = map(int, input().split())
    ab = []
    for i in range(N-1):
        a,b = map(int, input().split())
        ab.append((a,b))
    cd = []
    for i in range(Q):
        c,d = map(int, input().split())
        cd.append((c,d))
    return N,Q,ab,cd

if __name__ == '__main__':
    get_input()