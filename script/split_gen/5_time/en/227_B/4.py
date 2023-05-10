def main():
    n = int(input())
    s = list(map(int, input().split()))
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            a = (s[i] - s[j]) / 4
            b = s[i] / a - 3 * a
            if a > 0 and b > 0 and a.is_integer() and b.is_integer():
                print(n - 1)
                return
    print(n)
