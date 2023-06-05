Synthesizing 10/10 solutions

=======
Suggestion 1

def round_to_10(x,k):
    for i in range(k):
        if x % 10 != 0:
            x += 1
        else:
            x = x // 10
    return x

=======
Suggestion 2

def problem273_b(x, k):
    if k == 0:
        return x
    else:
        return round(x, -k)

x, k = map(int, input().split())
print(problem273_b(x, k))

=======
Suggestion 3

def my_round(num, n):
    if n == 0:
        return num

    i = 10 ** n
    if num % i == 0:
        return num

    return num + i - num % i

=======
Suggestion 4

def round_up(n, d):
    return (n//d+1)*d

x, k = map(int, input().split())
ans = x
for i in range(k):
    ans = round_up(ans, 10**(i+1))
print(ans)

=======
Suggestion 5

def main():
    X,K=map(int,input().split())
    for i in range(K):
        if X%10!=0:
            X+=1
        else:
            X=X//10
    print(X)

=======
Suggestion 6

def solve(x,k):
    if x==0:
        return 0
    res=x
    for i in range(1,k+1):
        tmp=round(x/(10**i))*(10**i)
        res=min(res,abs(x-tmp))
    return res

=======
Suggestion 7

def problem273_b(x, k):
    for i in range(k):
        x = int((x+5)/10)*10
    print(x)

=======
Suggestion 8

def main():
    x, k = map(int, input().split())
    for i in range(k):
        if x % (10 ** (i + 1)) < 5 * 10 ** i:
            print(x - x % (10 ** (i + 1)))
            break
    else:
        print(10 ** k)

=======
Suggestion 9

def problem273_b():
    x,k = map(int,input().split())
    print(x//10**k*10**k+10**k) if x%10**k>=5*10**(k-1) else print(x//10**k*10**k)

=======
Suggestion 10

def main():
    X, K = map(int, input().split())
    for i in range(K):
        X = (X+5)//10*10
    print(X)
