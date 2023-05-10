def main():
    n,m = map(int,input().split())
    for i in range(1,m+2-n):
        print(i,end=" ")
        for j in range(i+1,m+1):
            print(j,end=" ")
        print()
