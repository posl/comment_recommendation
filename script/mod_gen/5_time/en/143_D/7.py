def main():
    n = int(input())
    l = list(map(int, input().split()))
    l = sorted(l)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] + l[j] > l[k] and l[j] + l[k] > l[i] and l[k] + l[i] > l[j]:
                    count += 1
    print(count)

if __name__ == '__main__':
    main()