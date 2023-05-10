def main():
    n, m = map(int, input().split())
    a_list = []
    b_list = []
    for _ in range(m):
        a, b = map(int, input().split())
        a_list.append(a)
        b_list.append(b)
    a_list.reverse()
    b_list.reverse()
    ans = (n-1)*n//2
    ans_list = []
    for i in range(m):
        ans_list.append(ans)
        if a_list[i] > b_list[i]:
            a_list[i], b_list[i] = b_list[i], a_list[i]
        if a_list[i] == 1:
            ans -= n - b_list[i]
        elif b_list[i] == n:
            ans -= a_list[i] - 1
        else:
            ans -= a_list[i] - 1
            ans -= n - b_list[i]
    ans_list.reverse()
    for i in range(m):
        print(ans_list[i])

if __name__ == '__main__':
    main()