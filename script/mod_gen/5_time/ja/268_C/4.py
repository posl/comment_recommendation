def main():
    n = int(input())
    p = list(map(int, input().split()))
    p = [x-1 for x in p]
    count = 0
    for i in range(n):
        if p[i] == i:
            count += 1
            p[i] = -1
            if i != 0 and p[i-1] != -1:
                p[i-1] = -1
            elif i == 0 and p[n-1] != -1:
                p[n-1] = -1
            if i != n-1 and p[i+1] != -1:
                p[i+1] = -1
            elif i == n-1 and p[0] != -1:
                p[0] = -1
    print(count)

if __name__ == '__main__':
    main()