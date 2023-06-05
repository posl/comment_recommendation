def main():
    n = int(input())
    p = list(map(int, input().split()))
    p.insert(0, 0)
    max = 0
    for i in range(1, n+1):
        count = 0
        j = i
        while p[j] != -1:
            j = p[j]
            count += 1
        if count > max:
            max = count
    print(max+1)

if __name__ == '__main__':
    main()