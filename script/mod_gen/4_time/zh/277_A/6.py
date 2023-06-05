def main():
    line = input().split()
    N = int(line[0])
    X = int(line[1])
    P = input().split()
    for i in range(N):
        P[i] = int(P[i])
    for i in range(N):
        if P[i] == X:
            print(i+1)
            break

if __name__ == '__main__':
    main()