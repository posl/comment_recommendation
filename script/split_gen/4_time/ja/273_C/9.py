def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(-1)
    k = 0
    c = 1
    ans = [0] * n
    for i in range(n):
        if a[i] != a[i+1]:
            ans[k] = c
            k += 1
            c = 1
        else:
            c += 1
    print(*ans, sep="\n")
