def main():
    n,m = map(int,input().split())
    A = []
    for i in range(2*n):
        A.append(input())
    rank = [i for i in range(2*n)]
    for i in range(m):
        rank = sorted(rank,key=lambda x:(A[x][i],x))
    for i in rank[::-1]:
        print(i+1)
