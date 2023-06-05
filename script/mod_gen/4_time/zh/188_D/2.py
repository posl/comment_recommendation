def get_input():
    N,C = map(int,input().split())
    v = []
    for i in range(N):
        a,b,c = map(int,input().split())
        v.append((a,b,c))
    return N,C,v

if __name__ == '__main__':
    get_input()