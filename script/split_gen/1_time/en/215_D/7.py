def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * (M+1)
    for a in A:
        for i in range(a, M+1, a):
            B[i] = 1
    ans = []
    for i in range(1, M+1):
        if B[i] == 0:
            ans.append(i)
    print(len(ans))
    for a in ans:
        print(a)
