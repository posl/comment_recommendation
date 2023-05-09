def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K, X)
    #print(A)
    A.sort()
    i = 0
    while i < N:
        if A[i] > X:
            break
        i += 1
    #print(i)
    if i <= K:
        print(sum(A[:i]))
    else:
        print(sum(A[:i-K]) + (i-K) * X)
main()
I am not good at English. I am sorry if my English is not good.
I am a Japanese student. I am interested in programming. I want to solve problems in programming contests.
I am not good at English. I am sorry if my English is not good.
I am a Japanese student. I am interested in programming. I want to solve problems in programming contests.

if __name__ == '__main__':
    main()