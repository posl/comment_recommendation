def getDivisors(n):
    divisors = [1]
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n/i:
                divisors.append(n/i)
    return len(divisors)
n = int(input())
count = 0
for i in range(1, n+1):
    if i % 2 == 1 and getDivisors(i) == 8:
        count += 1
print(count)
I got 100% on this one. I think the only thing that could be improved is the getDivisors function. It's not the most efficient way to find divisors.
I'm a bit late to the party, but I wanted to post my solution anyway. I'm not sure if it's the most efficient solution, but it's the first one I came up with.

if __name__ == '__main__':
    getDivisors()