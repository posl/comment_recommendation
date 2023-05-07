def main():
    N = int(input())
    h = list(map(int,input().split()))
    count = 0
    for i in range(N):
        if h[i] > 0:
            count += 1
            for j in range(i,N):
                h[j] -= 1
    print(count)
main()

if __name__ == '__main__':
    main()