def divisors(n):
    count = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            count += 2
    if int(n**0.5)**2 == n:
        count -= 1
    return count
n = int(input())
count = 0
for i in range(1, n+1):
    if i % 2 == 1 and divisors(i) == 8:
        count += 1
print(count)
I'm not sure what the problem is. I'm trying to find the number of odd numbers with exactly eight positive divisors between 1 and N (inclusive). I'm doing this by creating a function that will count the number of divisors that a number has. Then I loop through all the numbers between 1 and N and count the number of odd numbers with 8 divisors. I'm not sure if this is the most efficient way to do this, but it works. I'm just not sure if it's the most efficient way to do this. Is there a better way to do this?
I'm not sure if this is the most efficient way to do this, but it works. I'm just not sure if it's the most efficient way to do this. Is there a better way to do this?
Of course there is. First, you don't need to check all the odd numbers between 1 and N . You only need to check the odd numbers between 1 and N/2 . Second, your divisors() function is inefficient. You can easily find the number of divisors of a number n by counting the powers of the prime factors of n . You can also do this in a more efficient way by using the fact that the number of divisors of n is equal to the product of (p+1) for all prime factors p .
I'm not sure if this is the most efficient way to do this, but it works. I'm just not sure if it's the most efficient way to do this. Is there a better way to do this? Of course there is. First, you don't need to check all the odd numbers between 1 and N . You only need to check the odd numbers between 1 and N/2 . Second, your divisors() function is inefficient. You can easily find the number of divisors of a number n by counting

if __name__ == '__main__':
    divisors()