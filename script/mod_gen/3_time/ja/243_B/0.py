def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_dict = {}
    b_dict = {}
    for i in range(n):
        a_dict[a[i]] = i
        b_dict[b[i]] = i
    ans1 = 0
    ans2 = 0
    for i in range(n):
        if a_dict[a[i]] == b_dict[a[i]]:
            ans1 += 1
        elif a_dict[a[i]] != b_dict[a[i]]:
            ans2 += 1
    print(ans1)
    print(ans2)

if __name__ == '__main__':
    main()