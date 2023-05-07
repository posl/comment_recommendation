def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(0, n):
        for j in range(0, n):
            if i != j:
                for k in range(0, n):
                    if i != k and j != k:
                        if a[i] * a[k] == a[j]:
                            count += 1
    print(count//2)

if __name__ == '__main__':
    main()