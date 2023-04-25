Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X = int(input())
    happiness = 0
    happiness += (X // 500) * 1000
    happiness += ((X % 500) // 5) * 5
    print(happiness)

=======
Suggestion 2

def main():
    X = int(input())
    print((X // 500) * 1000 + ((X % 500) // 5) * 5)

=======
Suggestion 3

def main():
    X = int(input())
    happiness = (X // 500) * 1000
    happiness += (X % 500) // 5 * 5
    print(happiness)

=======
Suggestion 4

def main():
    x = int(input())
    ans = (x // 500) * 1000
    x = x % 500
    ans += (x // 5) * 5
    print(ans)

=======
Suggestion 5

def main():
    X = int(input())
    print(1000 * (X // 500) + 5 * ((X % 500) // 5))

=======
Suggestion 6

def main():
    X = int(input())
    happiness = 0
    happiness += X//500 * 1000
    happiness += X%500//5 * 5
    print(happiness)

=======
Suggestion 7

def get_happiness_points(x):
    happiness_points = 0
    happiness_points += x // 500 * 1000
    happiness_points += x % 500 // 5 * 5
    return happiness_points

=======
Suggestion 8

def main():
    x = int(input())
    print(x//500*1000 + x%500//5*5)

main()

=======
Suggestion 9

def main():
    X = int(input())
    print(X//500*1000 + X%500//5*5)

=======
Suggestion 10

def main():
    x = int(input())
    print((x//500)*1000 + (x%500//5)*5)
