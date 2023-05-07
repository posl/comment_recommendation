def main():
    #Get the input
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #If N is 1 or less, then Takahashi can't remove any stones
    if N <= 1:
        print(0)
        return
    #If the largest number in A is 1, then Takahashi can remove 1 stone every turn
    if A[K-1] == 1:
        print(N-1)
        return
    #If the largest number in A is greater than 1, then Takahashi can remove the largest number in A
    #every turn until the pile is 1 stone, then he can remove 1 stone every turn
    else:
        #Find the number of turns it will take to get the pile to 1 stone
        turns = N // A[K-1]
        #Find the remaining number of stones
        remaining_stones = N % A[K-1]
        #If the remaining number of stones is 0, then Takahashi can remove A[K-1] stones every turn
        if remaining_stones == 0:
            print(A[K-1] * (turns-1))
        #If the remaining number of stones is 1, then Takahashi can remove A[K-1] stones every turn
        #until the pile is 1 stone, then he can remove 1 stone every turn
        elif remaining_stones == 1:
            print(A[K-1] * (turns-1) + 1)
        #If the remaining number of stones is greater than 1, then Takahashi can remove A[K-1] stones
        #every turn until the pile is 1 stone, then he can remove the remaining number of stones every turn
        else:
            print(A[K-1] * turns + remaining_stones - 1)

if __name__ == '__main__':
    main()