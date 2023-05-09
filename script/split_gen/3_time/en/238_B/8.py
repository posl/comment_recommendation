def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A = [360 - x for x in A]
    A.sort()
    A.append(360 + A[0])
    ans = 360
    for i in range(N):
        ans = min(ans, A[i + 1] - A[i])
    print(ans)
