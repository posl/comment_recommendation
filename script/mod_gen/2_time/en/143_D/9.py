def main():
    n = int(input())
    l = sorted(list(map(int, input().split())))
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] + l[j] > l[k]:
                    count += 1
    print(count)

if __name__ == '__main__':
    main()