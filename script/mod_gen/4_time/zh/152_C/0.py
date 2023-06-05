def problems152_c():
    N = int(input())
    P = list(map(int, input().split()))
    count = 1
    min = P[0]
    for i in range(1, N):
        if P[i] <= min:
            count += 1
        if P[i] < min:
            min = P[i]
    print(count)

if __name__ == '__main__':
    problems152_c()