def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    #Aの値に対応するindexを格納
    index = [[] for _ in range(N)]
    for i, a in enumerate(A):
        index[a-1].append(i)
    for l, r, x in query:
        #indexは0番目から始まるのでl-1,r-1
        print(len([i for i in index[x-1] if l-1 <= i <= r-1]))
