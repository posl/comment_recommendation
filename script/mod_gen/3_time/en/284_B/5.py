def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = [int(x) for x in input().split()]
        odd = 0
        for i in range(N):
            if A[i] % 2 == 1:
                odd += 1
        print(odd)

if __name__ == '__main__':
    main()