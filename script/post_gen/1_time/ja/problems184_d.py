Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    print(100.0 * (a * b + b * c + c * a) / (a + b + c) / (a + b + c))

=======
Suggestion 2

def main():
    A,B,C = map(int,input().split())
    print(100*(A/(A+B+C))+100*(B/(A+B+C))+100*(C/(A+B+C))-100)

=======
Suggestion 3

def main():
    A, B, C = map(int, input().split())
    print(A * B + B * C + C * A)

=======
Suggestion 4

def main():
    A,B,C = map(int,input().split())
    ans = 0
    for i in range(100):
        ans += (i+1)*(A/(A+B+C))
        ans += (i+1)*(B/(A+B+C))
        ans += (i+1)*(C/(A+B+C))
        A = A + A
        B = B + B
        C = C + C
    print(ans)

=======
Suggestion 5

def main():
    A,B,C = map(int, input().split())
    print(100*A/(A+B+C) + 100*B/(A+B+C))

=======
Suggestion 6

def main():
    A, B, C = map(int, input().split())
    print(100*(A*B+B*C+C*A)/(A+B+C)/(A*B+B*C+C*A))

=======
Suggestion 7

def main():
    a,b,c = map(int,input().split())
    ans = 0
    ans += a*(c/(a+b+c))
    ans += b*(c/(a+b+c))
    ans += c*(a+b+c-1)/(a+b+c)
    print(ans)

=======
Suggestion 8

def main():
    A,B,C = map(int,input().split())
    print(100*(A*B+B*C+C*A)/(A+B+C)/(A+B+C-1))

=======
Suggestion 9

def main():
    A, B, C = map(int, input().split())
    print(100*(A*(B+C)+B*C)/(A+B+C)**2)

=======
Suggestion 10

def main():
    A,B,C=map(int,input().split())
    ans=0
    for i in range(100):
        ans+=1
        for j in range(3):
            if i==99:
                ans+=100
                break
            if j==0:
                ans+=(A/(A+B+C))
                A+=A
            elif j==1:
                ans+=(B/(A+B+C))
                B+=B
            elif j==2:
                ans+=(C/(A+B+C))
                C+=C
    print(ans)
