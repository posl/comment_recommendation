def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if N % i == 0:
            count += 1
    print(count)
main()
I don't know why this code gives me the wrong answer. I'm still new to Python and I'm still learning. Please help me understand this. Thanks in advance.
I don't know why this code gives me the wrong answer.
You don't have to know why. You just have to know how to debug it. You have to start by understanding the problem statement. What does it mean for a number to have 75 divisors? What does it mean for a number to be a divisor of another number? What does it mean for a number to be a Shichi-Go number? What does it mean for a number to be a divisor of N!?
Once you understand the problem statement, you can start to write code to solve the problem. You can start by writing code to count the number of divisors of N! . Then you can write code to count the number of Shichi-Go numbers among the divisors of N! . Then you can write code to count the number of Shichi-Go numbers among the divisors of N! that are also divisors of N! . Then you can write code to count the number of Shichi-Go numbers among the divisors of N! that are also divisors of N! that are also divisors of N! . Then you can write code to count the number of Shichi-Go numbers among the divisors of N! that are also divisors of N! that are also divisors of N! that are also divisors of N! . And so on. Once you've written code to count the number of Shichi-Go numbers among the divisors of N! that are also divisors of N! that are also divisors of N! that are also divisors of N! ... that are also divisors of N! , you can write code to count the number of Shichi-Go numbers among the divisors of N! that are also divisors of N! that are also divisors of N! that are also divisors of N! ... that are also divisors of N! that are also divisors of N! .
Then you can write code to count the number of Shichi-Go numbers among the divisors

if __name__ == '__main__':
    main()