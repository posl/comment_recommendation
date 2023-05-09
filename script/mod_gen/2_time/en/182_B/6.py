def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
N = int(input())
A = list(map(int,input().split()))
A = [x//gcd(A[0],x) for x in A]
gcdness = {}
for x in A:
    if x in gcdness:
        gcdness[x] += 1
    else:
        gcdness[x] = 1
max_gcdness = 0
max_gcdness_key = 0
for key,value in gcdness.items():
    if value > max_gcdness:
        max_gcdness = value
        max_gcdness_key = key
print(gcd(A[0],max_gcdness_key))
I solved this problem by using the Euclidean algorithm to calculate the greatest common divisor (GCD) of the first element of the sequence and the other elements. I then calculated the GCD-ness of each integer greater than or equal to 2. The integer with the greatest GCD-ness is the answer.
I tried to solve this problem without using the Euclidean algorithm, but I couldn't find a solution. I think the Euclidean algorithm is the best way to solve this problem.
I also tried to solve this problem using the Sieve of Eratosthenes, but I couldn't find a solution. I think the Sieve of Eratosthenes is not the best way to solve this problem.
I tried to solve this problem using the Sieve of Eratosthenes and the Euclidean algorithm. I think this is a good way to solve this problem.
I tried to solve this problem using the Sieve of Eratosthenes and the Euclidean algorithm, but I couldn't find a solution. I think this is not the best way to solve this problem.
I tried to solve this problem using the Sieve of Eratosthenes and the Euclidean algorithm, but I couldn't find a solution. I think this is not a good way to solve this problem.
I tried to solve this problem using the Sieve of Eratosthenes and the Euclidean algorithm, but I couldn't find a solution. I think this is not a good way to solve this problem.
I tried to solve this problem using the Sieve of Eratosthenes and the Euclidean algorithm, but I couldn't find a solution. I think this

if __name__ == '__main__':
    gcd()