def main():
    line = input()
    line = line.split()
    N = int(line[0])
    X = int(line[1])
    line = input()
    line = line.split()
    L = [int(x) for x in line]
    D = [0]*(N+1)
    for i in range(1,N+1):
        D[i] = D[i-1]+L[i-1]
    D.append(D[N]+L[N-1])
    count = 0
    for i in range(N+1):
        if D[i] <= X:
            count += 1
    print(count)
    return 0

if __name__ == '__main__':
    main()