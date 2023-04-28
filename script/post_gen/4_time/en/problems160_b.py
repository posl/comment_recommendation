Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = int(input())
    print(1000 * (x // 500) + 5 * ((x % 500) // 5))

=======
Suggestion 2

def main():
    X = int(input())
    print(1000 * (X // 500) + 5 * ((X % 500) // 5))

=======
Suggestion 3

def main():
    x = int(input())
    print((x//500)*1000+((x%500)//5)*5)

=======
Suggestion 4

def main():
    X = int(input())
    print((X//500)*1000 + ((X%500)//5)*5)

=======
Suggestion 5

def main():
    # input
    X = int(input())

    # compute

    # output
    print(1000*(X//500) + 5*((X%500)//5))

=======
Suggestion 6

def main():
    x = int(input())
    print(x//500 * 1000 + (x%500)//5 * 5)

main()

=======
Suggestion 7

def solve(x):
    return (x//500)*1000+((x%500)//5)*5

=======
Suggestion 8

def main():
    # Take input Here and Call solution function
    x = int(input())
    print(solution(x))

=======
Suggestion 9

def gold_coins():
    x = int(input())
    if x < 500:
        print(x*2)
    elif x >= 500:
        print((x//500)*1000 + ((x%500)//5)*5)

gold_coins()
