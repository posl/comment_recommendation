def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    a_list.sort()
    ans = 0
    for i in range(n):
        ans += a_list[i] * (n - i - 1) - a_list[i] * i
    print(ans * 2)

if __name__ == '__main__':
    main()