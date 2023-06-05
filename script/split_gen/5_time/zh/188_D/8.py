def main():
    N,C = map(int,input().split())
    A = []
    B = []
    C = []
    for i in range(N):
        a,b,c = map(int,input().split())
        A.append(a)
        B.append(b)
        C.append(c)
    print(N,C,A,B,C)
