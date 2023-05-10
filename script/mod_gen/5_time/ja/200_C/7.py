def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_mod = [i % 200 for i in a]
    a_mod.sort()
    ans = 0
    cnt = 1
    for i in range(n - 1):
        if a_mod[i] == a_mod[i + 1]:
            cnt += 1
        else:
            ans += cnt * (cnt - 1) // 2
            cnt = 1
    ans += cnt * (cnt - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()