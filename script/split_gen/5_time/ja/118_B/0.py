def main():
    N, M = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split()))[1:])
    like = set(A[0])
    for a in A[1:]:
        like = like & set(a)
    print(len(like))
