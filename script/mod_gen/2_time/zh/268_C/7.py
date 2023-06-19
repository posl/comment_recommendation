def main():
    N = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if p[i] == (i-1)%N or p[i] == (i+1)%N:
            count += 1
    print(count)

if __name__ == '__main__':
    main()