def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    l.sort()
    left = l[0][0]
    right = l[0][1]
    for i in range(1, n):
        if l[i][0] <= right:
            right = max(right, l[i][1])
        else:
            print(left, right)
            left = l[i][0]
            right = l[i][1]
    print(left, right)

if __name__ == '__main__':
    main()