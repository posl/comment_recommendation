def main():
    n = int(input())
    a = list(map(int, input().split()))
    max = 0
    for i in range(n):
        for j in range(i, n):
            for k in range(1, a[j]+1):
                if k > max and min(a[i:j+1]) >= k:
                    max = k
    print(max)

if __name__ == '__main__':
    main()