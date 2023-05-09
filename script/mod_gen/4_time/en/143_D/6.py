def main():
    n = int(input())
    L = list(map(int, input().split()))
    L.sort()
    count = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if L[i] + L[j] > L[k]:
                    count += 1
    print(count)

if __name__ == '__main__':
    main()