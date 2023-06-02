Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    X = int(input())
    print(int(X/500)*1000 + int((X%500)/5)*5)

=======
Suggestion 2

def main():
    x = int(input())
    print(1000*(x//500)+5*((x%500)//5))

=======
Suggestion 3

def exchange(x):
    result = 0
    result += (x // 500) * 1000
    result += ((x % 500) // 5) * 5
    return result

=======
Suggestion 4

def main():
    x = int(input())
    print((x // 500)*1000 + ((x % 500) // 5)*5)

=======
Suggestion 5

def main():
    x = int(input())
    ans = 0
    ans += (x//500) * 1000
    x = x%500
    ans += (x//5)*5
    print(ans)

=======
Suggestion 6

def main():
    num = int(input())
    print(num//500*1000+(num%500)//5*5)

=======
Suggestion 7

def problem160_b():
    a = int(input())
    b = a//500
    c = a%500
    d = c//5
    e = c%5
    print(1000*b+5*d)
problem160_b()

=======
Suggestion 8

def main():
    x = int(input())
    y = x // 500
    z = (x - y * 500) // 5
    print(y * 1000 + z * 5)
