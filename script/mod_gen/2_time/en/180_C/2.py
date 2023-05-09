def divisor(n):
    i = 1
    result = []
    while i*i <= n:
        if n % i == 0:
            result.append(i)
            if i != n // i:
                result.append(n//i)
        i += 1
    return result
N = int(input())
divisors = divisor(N)
divisors.sort()
for d in divisors:
    print(d)
The input is an integer N (1≦N≦10^{12}).
The output is all possible number of people to which we can evenly distribute the cream puffs without cutting them.
The answer is the number of divisors of N.
I used the function divisor(n) to get the divisors of N.
The function divisor(n) returns the list of divisors of n.

if __name__ == '__main__':
    divisor()