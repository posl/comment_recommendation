Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    a, b, k = map(int, input().split())
    count = 0
    for i in range(100, 0, -1):
        if a % i == 0 and b % i == 0:
            count += 1
            if count == k:
                print(i)
                break

=======
Suggestion 2

def main():
    a, b, k = map(int, input().split())
    count = 0
    for i in range(min(a,b), 0, -1):
        if a % i == 0 and b % i == 0:
            count += 1
            if count == k:
                print(i)
                return

=======
Suggestion 3

def main():
    a, b, k = map(int, input().split())
    div = []
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            div.append(i)
    print(div[-k])

=======
Suggestion 4

def main():
    A, B, K = map(int, input().split())
    d = []
    for i in range(1, 101):
        if A % i == 0 and B % i == 0:
            d.append(i)
    print(d[-K])

=======
Suggestion 5

def main():
    a,b,k = map(int,input().split())
    list = []
    for i in range(1,101):
        if a % i == 0 and b % i == 0:
            list.append(i)
    print(list[-k])

=======
Suggestion 6

def get_divisor(a, b):
    divisor = []
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            divisor.append(i)
    return divisor

a, b, k = map(int, input().split())
divisor = get_divisor(a, b)
divisor.sort(reverse=True)
print(divisor[k - 1])

=======
Suggestion 7

def main():
    a, b, k = map(int, input().split())
    x = 0
    for i in range(1, 101):
        if a % i == 0 and b % i == 0:
            x += 1
            if x == k:
                print(i)
                break

=======
Suggestion 8

def main():
    a, b, k = map(int, input().split())
    i = 1
    ans = 0
    while True:
        if a % i == 0 and b % i == 0:
            ans += 1
            if ans == k:
                print(i)
                exit()
        i += 1

=======
Suggestion 9

def main():
    # input
    A, B, K = map(int, input().split())
    # compute
    list = []
    for i in range(1, min(A, B)+1):
        if A%i == 0 and B%i == 0:
            list.append(i)
    # output
    print(list[-K])
