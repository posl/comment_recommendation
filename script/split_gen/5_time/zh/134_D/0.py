def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    c = [0] * n
    for i in range(n):
        if a[i] == 1:
            b[i] = 1
            c[i] = 1
    for i in range(n):
        if b[i] == 1:
            for j in range(i + 1, n, i + 1):
                c[j] = 1 - c[j]
    ans = []
    for i in range(n):
        if c[i] == 1:
            ans.append(str(i + 1))
    print(len(ans))
    if len(ans) > 0:
        print(' '.join(ans))
