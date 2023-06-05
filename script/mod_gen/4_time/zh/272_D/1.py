def main():
    N,M = map(int,input().split())
    l = []
    for i in range(N):
        l.append([])
        for j in range(N):
            l[i].append(-1)
    l[0][0] = 0
    for i in range(N):
        for j in range(N):
            if l[i][j] != -1:
                if i - int(M**0.5) >= 0:
                    if l[i - int(M**0.5)][j] == -1:
                        l[i - int(M**0.5)][j] = l[i][j] + 1
                    elif l[i - int(M**0.5)][j] > l[i][j] + 1:
                        l[i - int(M**0.5)][j] = l[i][j] + 1
                if i + int(M**0.5) < N:
                    if l[i + int(M**0.5)][j] == -1:
                        l[i + int(M**0.5)][j] = l[i][j] + 1
                    elif l[i + int(M**0.5)][j] > l[i][j] + 1:
                        l[i + int(M**0.5)][j] = l[i][j] + 1
                if j - int(M**0.5) >= 0:
                    if l[i][j - int(M**0.5)] == -1:
                        l[i][j - int(M**0.5)] = l[i][j] + 1
                    elif l[i][j - int(M**0.5)] > l[i][j] + 1:
                        l[i][j - int(M**0.5)] = l[i][j] + 1
                if j + int(M**0.5) < N:
                    if l[i][j + int(M**0.5)] == -1:
                        l[i][j + int(M**0.5)] = l[i][j] + 1
                    elif l[i][j + int(M**0.5)] > l[i][j] + 1:
                        l[i][j + int(M**0.5)] = l[i][j] + 1
    for i in range(N):
        for j in range

if __name__ == '__main__':
    main()