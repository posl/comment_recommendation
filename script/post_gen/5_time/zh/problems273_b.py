Synthesizing 10/10 solutions

=======
Suggestion 1

def problem273_b():
    x,k = map(int,input().split())
    cur = x
    for i in range(k):
        cur = round(cur,-i)
    print(cur)

=======
Suggestion 2

def main():
    x,k = map(int,input().split())
    for i in range(k):
        if x%10 == 0:
            x = int(x/10)
        else:
            x += 10 - x%10
    print(x)

=======
Suggestion 3

def get_rounded_number(x,k):
    # print("x: %d, k: %d" % (x,k))
    # print("10^k: %d" % (10**k))
    # print("x / 10^k: %d" % (x / (10**k)))
    # print("(x / 10^k) * 10^k: %d" % ((x / (10**k)) * (10**k)))
    # print("x / 10^k * 10^k: %d" % ((x / (10**k)) * (10**k)))
    # print("(x / 10^k + 1) * 10^k: %d" % (((x / (10**k)) + 1) * (10**k)))
    # print("(x / 10^k + 1) * 10^k - x: %d" % ((((x / (10**k)) + 1) * (10**k)) - x))
    # print("x - (x / 10^k) * 10^k: %d" % (x - ((x / (10**k)) * (10**k))))
    # print("x - (x / 10^k) * 10^k: %d" % (x - ((x / (10**k)) * (10**k))))
    # print("x - (x / 10^k) * 10^k: %d" % (x - ((x / (10**k)) * (10**k))))
    # print("x - (x / 10^k) * 10^k: %d" % (x - ((x / (10**k)) * (10**k))))
    # print("x - (x / 10^k) * 10^k: %d" % (x - ((x / (10**k)) * (10**k))))
    # print("x - (x / 10^k) * 10^k: %d" % (x - ((x / (10**k)) * (10**k))))
    # print("x - (x / 10^k) * 10^k: %d" % (x - ((x /

=======
Suggestion 4

def problem273_b():
    x,k = map(int,input().split())
    for i in range(k):
        x = x//10*10+10
    print(x)

=======
Suggestion 5

def main():
    x,k = map(int,input().split())
    for i in range(k):
        x = (x+5)//10*10
    print(x)

=======
Suggestion 6

def main():
    x,k = input().split()
    x = int(x)
    k = int(k)
    for i in range(k):
        if x%10 == 0:
            x = x//10
        else:
            x = x+1
    print(x)

=======
Suggestion 7

def main():
    x, k = map(int, input().split())
    for i in range(k):
        if x % (10 ** (i + 1)) <= 5 * 10 ** i:
            print(x - x % (10 ** (i + 1)))
            return
    print(10 ** k)

=======
Suggestion 8

def roundUp(x, k):
    if k == 0:
        return x
    y = x
    if x % (10 ** k) >= 5 * (10 ** (k - 1)):
        y = x + 10 ** k - x % (10 ** k)
    else:
        y = x - x % (10 ** k)
    return y

=======
Suggestion 9

def main():
    x,k = map(int,input().split())
    a = 10**k
    b = x // a
    c = (b+1) * a
    print(c)

=======
Suggestion 10

def solution(x,k):
    for i in range(k):
        x = (x//10+1)*10 if x%10>=5 else (x//10)*10
    return x
