def main():
    #Read the input
    A,B,K = map(int,input().split())
    #If K is smaller than A, then Takahashi will eat K cookies, and Aoki will eat nothing.
    if K < A:
        A -= K
    #If K is larger than A, then Takahashi will eat all of his cookies, and Aoki will eat K-A cookies.
    elif K > A:
        B -= (K-A)
        A = 0
    #If K is equal to A, then Takahashi will eat all of his cookies, and Aoki will eat nothing.
    else:
        A = 0
    #Output the result
    print(A,B)

if __name__ == '__main__':
    main()