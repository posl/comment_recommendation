def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    if A[0] != 0:
        print(0)
        return
    for i in range(1,N):
        if A[i] - A[i-1] > 1:
            print(A[i-1]+1)
            return
    print(A[N-1]+1)
main()
The problem is that the code is not working for the first sample input given. The output is 0. The expected output is 4. I have no idea what I am doing wrong. Please help.
I am new to this so I am not sure if I am doing this right. I am trying to create a program that takes a list of numbers and then returns the sum of the list. I have the sum function working but I am not sure how to get the list to be inputted into the function. I am using a while loop to keep asking for input until the user inputs "done". I have tried using a list.append() function but that doesn't seem to work. Any help would be appreciated.
