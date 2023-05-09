def main():
    n, k = map(int, input().split())
    count = 0
    if k % 2 == 0:
        count += (n//k)**3
        if n%k >= k//2:
            count += (n//k+1)**3
    else:
        count += (n//k)**3
    print(count)
main()
