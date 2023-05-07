def main():
    N = int(input())
    A = []
    B = []
    for i in range(N-1):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    print(N-1)
    for i in range(N-1):
        print(i+1)
