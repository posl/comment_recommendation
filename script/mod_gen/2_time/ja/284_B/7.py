def main():
    #T = int(input())
    T = 4
    #for i in range(T):
    #    N = int(input())
    #    A = list(map(int, input().split()))
    N = 3
    A = [1,2,3]
    N = 2
    A = [20,23]
    N = 10
    A = [6,10,4,1,5,9,8,6,5,1]
    N = 1
    A = [1000000000]
    count = 0
    for j in range(N):
        if A[j] % 2 != 0:
            count += 1
    print(count)

if __name__ == '__main__':
    main()