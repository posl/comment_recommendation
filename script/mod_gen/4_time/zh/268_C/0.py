def main():
    N = int(input())
    p = list(map(int, input().split()))
    happiness = [0]*N
    for i in range(N):
        happiness[(p[i]-1)%N] += 1
    print(max(happiness))

if __name__ == '__main__':
    main()