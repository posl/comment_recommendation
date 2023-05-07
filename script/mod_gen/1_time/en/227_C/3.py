def main():
    n = int(input())
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        for j in range(i, int(n ** 0.5) + 1):
            if i * j > n:
                break
            for k in range(j, int(n ** 0.5) + 1):
                if i * j * k <= n:
                    if i == j == k:
                        count += 1
                    elif i == j or j == k:
                        count += 3
                    else:
                        count += 6
                else:
                    break
    print(count)

if __name__ == '__main__':
    main()