def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A_set = set(A)
    A_dict = {}
    for a in A:
        if a not in A_dict:
            A_dict[a] = 1
        else:
            A_dict[a] += 1
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if A[i] * A[j] in A_set:
                ans += A_dict[A[i] * A[j]]
    print(ans)
