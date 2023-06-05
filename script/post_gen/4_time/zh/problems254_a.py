Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    print(N%100)
    return

=======
Suggestion 2

def main():
    N = int(input())
    print(N%100)

=======
Suggestion 3

def print_last_two_digits(n):
    print(str(n)[-2:])

print_last_two_digits(254)
print_last_two_digits(101)

=======
Suggestion 4

def get_last_two_digits(number):
    return number % 100

=======
Suggestion 5

def last_two_digits():
    while True:
        try:
            n = int(input())
            print(n%100)
        except:
            break

=======
Suggestion 6

def print_last_two_digits(N):
    return N % 100

print(print_last_two_digits(254))
print(print_last_two_digits(101))

=======
Suggestion 7

def main():
    N = input()
    print(N[1:])

=======
Suggestion 8

def lastTwoDigits(num):
    return num % 100

=======
Suggestion 9

def main():
    n = int(input())
    print(n % 100)

main()

=======
Suggestion 10

def get_last_two_digits(num):
    if num < 100 or num > 999:
        return None
    return num % 100
