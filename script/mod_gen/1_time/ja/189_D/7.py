def main():
    N = int(input())
    S = [input() for _ in range(N)]
    count = 0
    for i in range(2**N):
        x = list(format(i, '0' + str(N) + 'b'))
        x = [True if x[i] == '1' else False for i in range(N)]
        y = [x[0]]
        for i in range(1, N):
            if S[i] == 'AND':
                y.append(y[i-1] and x[i])
            else:
                y.append(y[i-1] or x[i])
        if y[-1] == True:
            count += 1
    print(count)

if __name__ == '__main__':
    main()