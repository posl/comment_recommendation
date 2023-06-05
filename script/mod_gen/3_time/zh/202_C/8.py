def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    a_count = [0] * (n + 1)
    for i in a:
        a_count[i] += 1
    c_count = [0] * (n + 1)
    for i in c:
        c_count[i] += 1
    ans = 0
    for i in range(1, n + 1):
        ans += a_count[i] * c_count[i]
    print(ans)

if __name__ == '__main__':
    main()