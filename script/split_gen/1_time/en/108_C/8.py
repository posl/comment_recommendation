def main():
    n,k = map(int, input().split())
    if k%2 == 0:
        count = int(n/k)**3
        if k <= n:
            count += int((n-k//2)/k)**3
    else:
        count = int(n/k)**3
    print(count)
