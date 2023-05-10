def main():
    a, n = map(int, input().split())
    ans = -1
    for i in range(100):
        if n == 1:
            ans = i
            break
        if n % a == 0:
            n = n / a
        else:
            n -= 1
    print(int(ans))
