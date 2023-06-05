def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(lambda x: int(x)-1, input().split()))
    ca = [0] * n
    for i in range(n):
        ca[c[i]] += 1
    cb = [0] * n
    for i in range(n):
        cb[b[i]-1] += 1
    ans = 0
    for i in range(n):
        ans += ca[i] * cb[i]
    print(ans)

if __name__ == '__main__':
    main()