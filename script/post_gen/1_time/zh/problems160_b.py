Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = int(input())
    print(1000 * (x // 500) + 5 * ((x % 500) // 5))

=======
Suggestion 2

def main():
    x = int(input())
    coin500 = x // 500
    coin5 = (x % 500) // 5
    print(coin500 * 1000 + coin5 * 5)

=======
Suggestion 3

def main():
    x = int(input())
    print(x//500*1000+(x%500)//5*5)

=======
Suggestion 4

def main():
    x = int(input())
    print((x//500)*1000 + ((x%500)//5)*5)

=======
Suggestion 5

def problem160_b(x):
    #x = int(input())
    if x >= 500:
        a = x // 500
        b = x % 500
        if b >= 5:
            c = b // 5
            d = b % 5
            return a * 1000 + c * 5
        else:
            return a * 1000
    else:
        if x >= 5:
            c = x // 5
            d = x % 5
            return c * 5
        else:
            return 0
print(problem160_b(1024))
print(problem160_b(0))
print(problem160_b(1000000000))

=======
Suggestion 6

def main():
    x = int(input())
    y500 = x // 500
    y5 = (x % 500) // 5
    print(y500 * 1000 + y5 * 5)

=======
Suggestion 7

def main():
    x = int(input())
    ans = (x//500)*1000
    x = x%500
    ans += (x//5)*5
    print(ans)
