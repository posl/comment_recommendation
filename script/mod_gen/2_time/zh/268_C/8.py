def main():
    N = int(input())
    P = list(map(int, input().split()))
    P = [i-1 for i in P]
    count = 0
    for i in range(N):
        if i == P[P[i]]:
            count += 1
    if count == N:
        print(N)
    else:
        print(count-1)

if __name__ == '__main__':
    main()