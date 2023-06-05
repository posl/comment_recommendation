def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a.sort(reverse=True)
    b.sort(reverse=True)
    ans = 0
    for i in range(n):
        if a[i] > b[i]:
            ans += 1
    print(ans)
