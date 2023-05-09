def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    ans = "No"
    for i in range(n):
        if a[i] <= x and b[i] > 0:
            ans = "Yes"
            break
    print(ans)
