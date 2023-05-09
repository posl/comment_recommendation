def problem179_c():
    N = int(input())
    #print(N)
    count = 0
    for a in range(1, N):
        for b in range(1, N):
            c = N - a * b
            if c > 0:
                count += 1
            else:
                break
    print(count)

if __name__ == '__main__':
    problem179_c()