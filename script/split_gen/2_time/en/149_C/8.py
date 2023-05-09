def is_prime(num):
    if num == 2:
        return True
    elif num < 2 or num % 2 == 0:
        return False
    else:
        for i in range(3, int(num**0.5)+1, 2):
            if num % i == 0:
                return False
        return True
X = int(input())
while True:
    if is_prime(X):
        print(X)
        exit()
    else:
        X += 1
The idea is to use a function to check if a number is prime or not. Then, use a while loop to check if the number is prime or not. If it is not, add 1 to the number and check again. If it is, print the number and exit the program.
The function is_prime() checks if a number is prime or not. If the number is 2, return True. If the number is less than 2 or if the number is divisible by 2, return False. Otherwise, use a for loop to check if the number is divisible by any number between 3 and the square root of the number plus 1. If it is divisible by any number, return False. Otherwise, return True.
The while loop checks if the number is prime or not. If it is not, add 1 to the number and check again. If it is, print the number and exit the program.
The code above got accepted.
