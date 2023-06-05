def get_input():
    N,X = map(int,input().split())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    return N,X,A,B

if __name__ == '__main__':
    get_input()