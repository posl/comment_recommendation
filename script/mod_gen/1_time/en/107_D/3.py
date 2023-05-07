def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    for i in range(N):
        B.append((A[i], i))
    B.sort()
    C = [0] * N
    for i in range(N):
        C[B[i][1]] = i
    print(C)
    #print(B)
main()
I have a list of tuples, and I want to sort it by the second element of each tuple. I tried the following code, but it doesn't work. I get the error: TypeError: 'tuple' object does not support item assignment.
I have a list of tuples, and I want to sort it by the second element of each tuple. I tried the following code, but it doesn't work. I get the error: TypeError: 'tuple' object does not support item assignment. How do I fix this?

if __name__ == '__main__':
    main()