def main():
    N, M = map(int, input().split())
    A = [set() for i in range(M)]
    for i in range(M):
        k, *x = map(int, input().split())
        for j in range(k):
            A[i].add(x[j])
    for i in range(M):
        for j in range(i+1, M):
            if A[i] & A[j]:
                print("Yes")
                return
    print("No")
