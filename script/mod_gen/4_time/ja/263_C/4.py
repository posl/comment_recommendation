def main():
    n,m = map(int, input().split())
    for i in range(1, m+1):
        for j in range(1, m+1):
            if i >= j:
                continue
            for k in range(1, m+1):
                if j >= k:
                    continue
                print(i, j, k)

if __name__ == '__main__':
    main()