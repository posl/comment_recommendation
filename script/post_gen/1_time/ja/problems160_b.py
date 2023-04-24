Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = int(input())
    ans = 0
    ans += x // 500 * 1000
    ans += (x % 500) // 5 * 5
    print(ans)

=======
Suggestion 2

def main():
    X = int(input())
    print(X // 500 * 1000 + X % 500 // 5 * 5)

=======
Suggestion 3

def main():
    x = int(input())
    print(1000 * (x // 500) + 5 * ((x % 500) // 5))

=======
Suggestion 4

def main():
    x = int(input())
    print((x//500)*1000 + (x%500//5)*5)

main()

=======
Suggestion 5

def main():
    x = int(input())
    print((x//500)*1000 + ((x%500)//5)*5)

=======
Suggestion 6

def main():
    X = int(input())
    print((X//500)*1000 + ((X%500)//5)*5)

=======
Suggestion 7

def main():
    x = int(input())
    print(x//500*1000 + x%500//5*5)

=======
Suggestion 8

def main():
    X = int(input())
    print(1000*(X//500)+5*((X%500)//5))
