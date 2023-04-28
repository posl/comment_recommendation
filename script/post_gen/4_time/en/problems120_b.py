Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, K = map(int, input().split())
    divs = []
    for i in range(1, min(A, B) + 1):
        if A % i == 0 and B % i == 0:
            divs.append(i)
    print(divs[-K])

=======
Suggestion 2

def main():
    A, B, K = map(int, input().split())
    count = 0
    for i in range(max(A,B), 0, -1):
        if A % i == 0 and B % i == 0:
            count += 1
            if count == K:
                print(i)
                break

=======
Suggestion 3

def main():
    A, B, K = map(int, input().split())
    common = []
    for i in range(1, min(A, B) + 1):
        if A % i == 0 and B % i == 0:
            common.append(i)
    print(common[-K])

=======
Suggestion 4

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 5

def main():
    A, B, K = map(int, input().split())
    c = 0
    for i in range(1, max(A, B) + 1):
        if A % i == 0 and B % i == 0:
            c += 1
            if c == K:
                print(i)
                break

main()

=======
Suggestion 6

def main():
    A, B, K = map(int, input().split())
    divisors = [i for i in range(1, min(A, B) + 1) if A % i == B % i == 0]
    print(divisors[-K])

=======
Suggestion 7

def main():
    a, b, k = map(int, input().split())
    ans = 0
    cnt = 0
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            cnt += 1
            if cnt == k:
                ans = i
                break
    print(ans)

=======
Suggestion 8

def main():
  A, B, K = map(int, input().split())
  d = []
  for i in range(1, min(A, B) + 1):
    if A % i == 0 and B % i == 0:
      d.append(i)
  print(d[-K])

=======
Suggestion 9

def main():
    a,b,k = map(int,input().split())
    dividers = []
    for i in range(1,min(a,b)+1):
        if a%i == 0 and b%i == 0:
            dividers.append(i)
    print(dividers[-k])

=======
Suggestion 10

def main():
    a,b,k = map(int,input().split())
    count = 0
    for i in range(1,100):
        if a%i==0 and b%i==0:
            count += 1
            if count == k:
                print(i)
                return
