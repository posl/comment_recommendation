def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N, A)
    maxA = max(A)
    #print(maxA)
    if maxA > N:
        print(0)
    else:
        print(maxA)

if __name__ == '__main__':
    main()