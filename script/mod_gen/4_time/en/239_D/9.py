def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1): # i*i <= n
        if n % i == 0:
            return False
    return True
A, B, C, D = map(int, input().split())
for i in range(1, 100):
    if A <= A+i <= B and C <= A+i <= D and isPrime(A+i):
        print("Aoki")
        break
    elif A <= B-i <= B and C <= B-i <= D and isPrime(B-i):
        print("Aoki")
        break
    elif A <= C+i <= B and C <= C+i <= D and isPrime(C+i):
        print("Aoki")
        break
    elif A <= D-i <= B and C <= D-i <= D and isPrime(D-i):
        print("Aoki")
        break
    elif A+i > B:
        print("Takahashi")
        break
    elif B-i < A:
        print("Takahashi")
        break
    elif C+i > D:
        print("Takahashi")
        break
    elif D-i < C:
        print("Takahashi")
        break

if __name__ == '__main__':
    isPrime()