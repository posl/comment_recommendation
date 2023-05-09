def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(0)
    ans = [0] * N
    ans[0] = 1
    count = 0
    for i in range(N):
        if A[i] != A[i+1]:
            ans[count] += 1
            count = 0
        else:
            count += 1
    print("\n".join(map(str, ans)))
