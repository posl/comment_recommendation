def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    count = 0
    for i in range(N):
        for j in range(i+1,N):
            if (A[i]-A[j])%200 == 0:
                count += 1
    print(count)

if __name__ == '__main__':
    main()