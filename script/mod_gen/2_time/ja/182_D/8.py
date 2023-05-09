def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(A)
    A.sort(reverse=True)
    #print(A)
    #print(sum(A))
    if sum(A) <= 0:
        print(0)
    else:
        print(sum(A[:N-1]))

if __name__ == '__main__':
    main()