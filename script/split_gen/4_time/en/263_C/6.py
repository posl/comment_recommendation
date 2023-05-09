def main():
    N,M = map(int,input().split())
    for i in range(1,M+1):
        print(i,end=" ")
    print()
    for i in range(1,M):
        if i%2==0:
            print(i,end=" ")
    print(M)
    for i in range(1,M):
        if i%2==1:
            print(i,end=" ")
    print(M)
