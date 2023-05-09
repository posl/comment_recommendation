def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(lambda x: int(x) - 1, input().split()))
    count = [0] * n
    for i in range(n):
        count[b[c[i]]] += 1
    ans = 0
    for i in range(n):
        ans += count[a[i]]
    print(ans)

if __name__ == '__main__':
    main()