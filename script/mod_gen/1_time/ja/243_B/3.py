def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_dict = {a[i]: i for i in range(n)}
    b_dict = {b[i]: i for i in range(n)}
    ans1 = 0
    ans2 = 0
    for i in range(n):
        if a[i] == b[i]:
            ans1 += 1
        elif a_dict[b[i]] == i:
            ans2 += 1
    print(ans1)
    print(ans2)

if __name__ == '__main__':
    main()