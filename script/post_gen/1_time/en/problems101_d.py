Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    k = int(input())
    snuke = [1]
    for i in range(k):
        print(snuke[i])
        snuke.append(snuke[i]*10)
        snuke.append(snuke[i]*10+1)

main()

This code is a bit slow, but it works. I tried to solve this problem in a more efficient way, but I couldn’t. I’ll try to solve it later.

I got 100 points for this problem.

=======
Suggestion 2

def f(n):
    s = str(n)
    sum = 0
    for i in s:
        sum += int(i)
    return sum

=======
Suggestion 3

def S(n):
    return sum(int(i) for i in str(n))

=======
Suggestion 4

def sum_digits(n):
    return sum([int(x) for x in str(n)])

=======
Suggestion 5

def sum_digits(n):
    return sum([int(d) for d in str(n)])

=======
Suggestion 6

def sum_digits(n):
    return sum(int(c) for c in str(n))

=======
Suggestion 7

def digit_sum(n):
    return sum(int(i) for i in str(n))

=======
Suggestion 8

def s(n):
    return sum(map(int, list(str(n))))

=======
Suggestion 9

def s(n):
    return sum(map(int, str(n)))

=======
Suggestion 10

def findSnukeNum(K):
    # 1 is a snuke number
    snukeNums = [1]
    # Keep track of the next snuke number to add
    nextNum = 2
    # Keep track of the sum of the digits of the next snuke number
    nextSum = 2
    # Keep track of the sum of the digits of the last snuke number added
    lastSum = 1
    # Keep track of the last snuke number added
    lastNum = 1
    # Keep track of the sum of the digits of the last snuke number added
    lastSum = 1
    # Keep track of the sum of the digits of the next snuke number to add
    nextSum = 2
    # Keep track of the next snuke number to add
    nextNum = 2
    # Keep track of the sum of the digits of the last snuke number added
    lastSum = 1
    # Keep track of the last snuke number added
    lastNum = 1
    # While we have not found K snuke numbers
    while len(snukeNums) < K:
        # If the next snuke number is less than the last snuke number added
        if nextNum < lastNum:
            # Add the next snuke number to the list
            snukeNums.append(nextNum)
            # Increase the sum of the digits of the next snuke number
            nextSum += 1
            # Increase the next snuke number
            nextNum += 1
        # If the next snuke number is greater than the last snuke number added
        elif nextNum > lastNum:
            # Add the next snuke number to the list
            snukeNums.append(nextNum)
            # Increase the sum of the digits of the next snuke number
            nextSum += 1
            # Increase the next snuke number
            nextNum += 1
        # If the next snuke number is equal to the last snuke number added
        else:
            # If the sum of the digits of the next snuke number is greater than the sum of the digits of the last snuke number added
            if nextSum > lastSum:
                # Add the next snuke number to the list
                snukeNums.append
