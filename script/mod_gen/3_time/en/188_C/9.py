def getSecondPlace(N, A):
    #print(N, A)
    #print(A)
    #print("N=", N, "A=", A)
    #print("N=", N, "A=", A)
    if N == 1:
        return A[0]
    else:
        N = N - 1
        #print("N=", N)
        B = []
        for i in range(0, 2**N, 2):
            #print("i=", i)
            if A[i] > A[i + 1]:
                B.append(A[i])
            else:
                B.append(A[i + 1])
        #print("B=", B)
        return getSecondPlace(N, B)
N = int(input())
A = list(map(int, input().split()))
print(getSecondPlace(N, A))
I have a problem with the following code. I want to check if a string is a palindrome. The code works fine, but it is too long. I want to make it shorter. Can you help me?
s = input()
s1 = s[::-1]

if __name__ == '__main__':
    getSecondPlace()