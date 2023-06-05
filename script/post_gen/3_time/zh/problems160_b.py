Synthesizing 10/10 solutions

=======
Suggestion 1

def get_coin_num(x):
    coin_num = 0
    coin_num += x // 500 * 1000
    x = x % 500
    coin_num += x // 5 * 5
    return coin_num

=======
Suggestion 2

def main():
    x = int(input())
    a = x // 500
    b = x % 500
    c = b // 5
    print(a * 1000 + c * 5)

=======
Suggestion 3

def max_happy(x):
    happy = 0
    while x >= 500:
        x -= 500
        happy += 1000
    while x >= 5:
        x -= 5
        happy += 5
    return happy

=======
Suggestion 4

def main():
    x = int(input())
    y500 = x // 500
    y5 = x % 500 // 5
    print(y500 * 1000 + y5 * 5)

=======
Suggestion 5

def main():
    x = int(input())
    print(x//500*1000+(x%500)//5*5)

=======
Suggestion 6

def main():
    x = int(input())
    print(int(x/500)*1000 + int((x%500)/5)*5)

=======
Suggestion 7

def main():
    x = int(input())
    print(1000*(x//500)+5*((x%500)//5))

=======
Suggestion 8

def main():
    X = int(input())
    happiness = 0
    happiness += (X // 500) * 1000
    happiness += ((X % 500) // 5) * 5
    print(happiness)

=======
Suggestion 9

def main():
    x = int(input())
    ans = 0
    ans += (x // 500) * 1000
    x %= 500
    ans += (x // 5) * 5
    print(ans)

=======
Suggestion 10

def main():
    x = int(input())
    #print(x)
    #print(type(x))
    #print(x//500)
    #print(x%500)
    #print((x%500)//5)
    #print((x%500)%5)
    print((x//500)*1000 + ((x%500)//5)*5)
