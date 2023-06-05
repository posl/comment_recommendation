def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 'YES'
    for i in range(n):
        if p[i] != i+1:
            ans = 'NO'
    print(ans)

if __name__ == '__main__':
    main()