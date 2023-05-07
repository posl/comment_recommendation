def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    max_even = -1
    for i in range(n-1, 0, -1):
        if a[i] % 2 == 0:
            if a[i] == a[i-1]:
                max_even = a[i]
                break
            elif a[i] - 1 == a[i-1]:
                max_even = a[i]
                break
    print(max_even)
