def main():
    n = int(input())
    a = [0 for _ in range(n+1)]
    b = [0 for _ in range(n+1)]
    for i in range(n-1):
        a[i+1], b[i+1] = map(int, input().split())
    count = [0 for _ in range(n+1)]
    for i in range(1, n):
        count[a[i]] += 1
        count[b[i]] += 1
    for i in range(1, n+1):
        if count[i] == n-1:
            print("Yes")
            return
    print("No")

if __name__ == '__main__':
    main()