def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    b_count = [0] * n
    for i in range(n):
        b_count[b[c[i] - 1] - 1] += 1
    ans = 0
    for i in range(n):
        ans += b_count[a[i] - 1]
    print(ans)

if __name__ == '__main__':
    main()