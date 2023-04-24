Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = int(input())
    print((x // 500) * 1000 + ((x % 500) // 5) * 5)

=======
Suggestion 2

def main():
    x = int(input())
    print(x // 500 * 1000 + x % 500 // 5 * 5)

main()

=======
Suggestion 3

def get_happiness(x):
    happiness = 0
    happiness += (x // 500) * 1000
    x = x % 500
    happiness += (x // 5) * 5
    return happiness

x = int(input())
print(get_happiness(x))

=======
Suggestion 4

def main():
    x = int(input())
    print(1000 * (x // 500) + 5 * ((x % 500) // 5))

=======
Suggestion 5

def main():
    X = int(input())
    print((X//500)*1000+((X%500)//5)*5)

=======
Suggestion 6

def happiness_points(x):
    return 1000 * (x // 500) + 5 * (x % 500 // 5)

=======
Suggestion 7

def happiness(x):
    return x//500*1000 + x%500//5*5

=======
Suggestion 8

def main():
    # This is a placeholder for a solution.
    print("Hello World!")
