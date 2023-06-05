def main():
    n = int(input())
    A = [int(i) for i in input().split()]
    ans = [0] * 10
    for i in range(n):
        ans[A[i]] += 1
    for i in range(10):
        print(ans[i])
