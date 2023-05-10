def main():
    n, k, a = map(int, input().split())
    if k <= n:
        print(k)
    else:
        k = k - n
        while k > 0:
            a += 1
            k -= 1
            if a == n + 1:
                a = 1
        print(a)
