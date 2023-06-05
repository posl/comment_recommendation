def main():
    N,M = map(int,input().split())
    A = []
    for i in range(N):
        A.append(list(map(int,input().split()))[1:])
    like = set(A[0])
    for i in range(1,N):
        like = like & set(A[i])
    print(len(like))
main()
