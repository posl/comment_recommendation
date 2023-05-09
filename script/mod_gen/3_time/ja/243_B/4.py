def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_dict = dict(zip(a, range(n)))
    b_dict = dict(zip(b, range(n)))
    count1 = 0
    count2 = 0
    for i in range(n):
        if a[i] in b_dict and a_dict[a[i]] == b_dict[a[i]]:
            count1 += 1
        if a[i] in b_dict and a_dict[a[i]] != b_dict[a[i]]:
            count2 += 1
    print(count1)
    print(count2)

if __name__ == '__main__':
    main()