def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    a_list.sort()
    b_list.sort()
    ans = 10**9
    for a in a_list:
        for b in b_list:
            ans = min(ans, abs(a-b))
    print(ans)

if __name__ == '__main__':
    main()