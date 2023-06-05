def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    i = 0
    while k > 0:
        if i == n:
            i = 0
        k -= 1
        i = a[i] - 1
    print(i + 1)
