def main():
    N, M = map(int, input().split())
    x = [0] * M
    y = [0] * M
    for i in range(M):
        x[i], y[i] = map(int, input().split())
    
    count = 0
    for a in range(1, N - 1):
        for b in range(a + 1, N):
            for c in range(b + 1, N + 1):
                if (a in x and b in y) or (a in y and b in x):
                    if (b in x and c in y) or (b in y and c in x):
                        if (c in x and a in y) or (c in y and a in x):
                            count += 1
    print(count)

if __name__ == '__main__':
    main()