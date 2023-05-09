def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    ans = 0
    for i in range(n):
        ans += a[i] / b[i]
    ans /= 2
    print(ans)
