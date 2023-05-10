def main():
    N = int(input())
    A = list(map(int,input().split()))
    print(sum([A[i]-1 for i in range(N)]))

if __name__ == '__main__':
    main()