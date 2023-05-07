def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    d = {}
    for a in A:
        d[a] = d.get(a, 0) + 1
    for i in range(N):
        ans[i] = sum([d[a] for a in d if a != A[i]])
    for a in ans:
        print(a // 2)
