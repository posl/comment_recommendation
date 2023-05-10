def main():
    N = int(input())
    p = list(map(int, input().split()))
    happy = 0
    for i in range(N):
        if p[i] == i:
            happy += 1
            if i < N-1 and p[i+1] == i+1:
                p[i], p[i+1] = p[i+1], p[i]
            elif i == N-1:
                p[i], p[0] = p[0], p[i]
    print(happy)

if __name__ == '__main__':
    main()