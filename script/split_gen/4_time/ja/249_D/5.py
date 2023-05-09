def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A_set = set(A)
    A_dict = {}
    for i in range(N):
        if A[i] not in A_dict:
            A_dict[A[i]] = []
        A_dict[A[i]].append(i)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if A[i]*A[j] in A_set:
                ans += len(A_dict[A[i]*A[j]])
    print(ans)
