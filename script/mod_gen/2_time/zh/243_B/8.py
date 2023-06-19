def main():
    n = int(input())
    a = input().split()
    b = input().split()
    a = [int(i) for i in a]
    b = [int(i) for i in b]
    count_1 = 0
    count_2 = 0
    for i in range(n):
        if a[i] == b[i]:
            count_1 += 1
    for i in range(n):
        for j in range(n):
            if a[i] == b[j] and i != j:
                count_2 += 1
    print(count_1)
    print(count_2)

if __name__ == '__main__':
    main()