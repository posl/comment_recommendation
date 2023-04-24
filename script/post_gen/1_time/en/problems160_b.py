Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    X = int(input())
    print((X // 500) * 1000 + ((X % 500) // 5) * 5)

=======
Suggestion 2

def main():
    X = int(input())
    happiness = 0
    happiness += X // 500 * 1000
    happiness += X % 500 // 5 * 5
    print(happiness)

=======
Suggestion 3

def main():
    X = int(input())
    ans = 0
    ans += X // 500 * 1000
    X = X % 500
    ans += X // 5 * 5
    print(ans)

=======
Suggestion 4

def main():
    X = int(input())
    print((X // 500) * 1000 + (X % 500) // 5 * 5)

main()

=======
Suggestion 5

def main():
    x = int(input())
    print(1000 * (x // 500) + 5 * ((x % 500) // 5))

main()

=======
Suggestion 6

def main():
    X = int(input())
    print((X//500)*1000 + (X%500//5)*5)

=======
Suggestion 7

def main():
    X = int(input())
    print(X//500*1000+X%500//5*5)

=======
Suggestion 8

def happiness(x):
    return (x//500)*1000 + (x%500//5)*5

=======
Suggestion 9

def happiness(x):
    return (x//500)*1000 + (x%500)//5*5
