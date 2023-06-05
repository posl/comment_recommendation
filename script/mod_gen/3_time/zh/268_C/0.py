def main():
    N = int(input())
    p = [int(x) for x in input().split()]
    count = 0
    for i in range(N):
        if p[p[i]] == i:
            count += 1
    print(count)

if __name__ == '__main__':
    main()