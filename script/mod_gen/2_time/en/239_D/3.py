def is_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
A, B, C, D = map(int, input().split())
for i in range(A, B+1):
    for j in range(C, D+1):
        if is_prime(i+j):
            print("Aoki")
            exit()
print("Takahashi")
This is my code. It works for the first two test cases, but it times out for the third one. I know that the third test case is just asking for Takahashi to win, so I tried to make the code only check if the sum of A and C is a prime, but that didn't work. Can someone explain to me why my code is timing out?
You can use the Sieve of Eratosthenes to generate a list of primes. You can then use that list to check if the sum of two numbers is prime.
This is a very naive solution, but it works. You can improve it by using the Sieve of Eratosthenes to generate a list of primes.

if __name__ == '__main__':
    is_prime()