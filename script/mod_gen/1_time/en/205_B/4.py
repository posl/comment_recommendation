def main():
    #read input
    N = int(input())
    A = list(map(int, input().split()))
    #check if A is a permutation of (1, 2, ..., N)
    if sorted(A) == list(range(1, N+1)):
        print("Yes")
    else:
        print("No")
main()

if __name__ == '__main__':
    main()