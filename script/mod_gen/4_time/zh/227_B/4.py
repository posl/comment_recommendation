def main():
    N = int(input())
    S = list(map(int,input().split()))
    count = 0
    for i in range(N):
        for j in range(1,32):
            for k in range(1,32):
                if S[i] == 4*j*k+3*j+3*k:
                    count += 1
    print(N-count)

if __name__ == '__main__':
    main()