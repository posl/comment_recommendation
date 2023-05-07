def main():
    N = int(input())
    P = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if P[i] == min(P[:i+1]):
            count += 1
    print(count)

if __name__ == '__main__':
    main()