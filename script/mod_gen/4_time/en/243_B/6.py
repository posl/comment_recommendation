def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    count = 0
    for i in range(n):
        if a[i] == b[i]:
            count += 1
    b_dict = {}
    for i in range(n):
        b_dict[b[i]] = i
    count2 = 0
    for i in range(n):
        if a[i] in b_dict and b_dict[a[i]] != i:
            count2 += 1
    print(count)
    print(count2)

if __name__ == '__main__':
    main()