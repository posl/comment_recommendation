Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, x = map(int, input().split())
    if a * 10 ** 9 + b * 10 <= x:
        print(10 ** 9)
        return
    l = 0
    r = 10 ** 9
    while r - l > 1:
        m = (l + r) // 2
        if a * m + b * len(str(m)) <= x:
            l = m
        else:
            r = m
    print(l)

=======
Suggestion 2

def main():
    A, B, X = map(int, input().split())
    if A * 10**9 + B * 10 <= X:
        print(10**9)
        return

    ans = 0
    for i in range(1, 10):
        if A * 10**(i-1) + B * i <= X:
            ans = 10**(i-1)
        else:
            break
    if ans == 0:
        print(0)
        return

    for i in range(1, 10):
        if A * 10**(i-1) + B * i <= X:
            ans += 1
        else:
            break

    print(ans)

=======
Suggestion 3

def main():
    A, B, X = map(int, input().split())
    #print(A, B, X)
    left = 0
    right = 10 ** 9 + 1
    while right - left > 1:
        mid = (left + right) // 2
        if A * mid + B * len(str(mid)) <= X:
            left = mid
        else:
            right = mid
    print(left)

=======
Suggestion 4

def main():
    A, B, X = map(int, input().split())
    if A == B:
        print(X // A)
    elif A > B:
        if X >= A:
            print(X // A)
        else:
            print(0)
    else:
        # A < B
        if X >= A:
            print(X // A)
        else:
            print(0)

=======
Suggestion 5

def  main():
    A, B, X = map(int, input().split())
    if A * 10**9 + B * 10 < X:
        print(0)
        return
    if A + B > X:
        print(0)
        return

    min = 1
    max = 10**9
    while max - min > 1:
        mid = (max + min) // 2
        if A * mid + B * (len(str(mid))) <= X:
            min = mid
        else:
            max = mid

    print(min)

=======
Suggestion 6

def   main ():
    A ,  B ,  X  =  map ( int ,  input (). split ())
    if  A  *  10 ** 9  +  B  *  10  <=  X :
         print ( 0 )
    else :
        left  =  0 
        right  =  10 ** 9 
         while  right  -  left  >  1 :
            mid  =  ( left  +  right ) // 2 
             if  A  *  mid  +  B  *  len ( str ( mid )) <=  X :
                left  =  mid 
             else :
                right  =  mid 
         print ( left )

=======
Suggestion 7

def main():
    A, B, X = map(int, input().split())

    # 1 <= N <= 10^9
    # N = 10^9
    # A*N + B*d(N) <= X
    # A*10^9 + B*10 <= X
    # 10^9*A + 10*B <= X
    # 10^9*A <= X - 10*B
    # N <= (X -

=======
Suggestion 8

def main():
    A, B, X = map(int, input().split())
    #print(A, B, X)
    #print(10**9)
    #print(X//(A+B))
    #print(X//(A+B)+1)
    #print(X//(A+B)-1)
    #print(X//(A+B)+2)
    #print(X//(A+B)-2)
    #print(X//(A+B)+3)
    #print(X//(A+B)-3)
    #print(X//(A+B)+4)
    #print(X//(A+B)-4)
    #print(X//(A+B)+5)
    #print(X//(A+B)-5)
    #print(X//(A+B)+6)
    #print(X//(A+B)-6)
    #print(X//(A+B)+7)
    #print(X//(A+B)-7)
    #print(X//(A+B)+8)
    #print(X//(A+B)-8)
    #print(X//(A+B)+9)
    #print(X//(A+B)-9)
    #print(X//(A+B)+10)
    #print(X//(A+B)-10)
    #print(X//(A+B)+11)
    #print(X//(A+B)-11)
    #print(X//(A+B)+12)
    #print(X//(A+B)-12)
    #print(X//(A+B)+13)
    #print(X//(A+B)-13)
    #print(X//(A+B)+14)
    #print(X//(A+B)-14)
    #print(X//(A+B)+15)
    #print(X//(A+B)-15)
    #print(X//(A+B)+16)
    #print(X//(A+B)-16)
    #print(X//(A+B)+17)
    #print(X//(A+B)-17)
    #print(X//(A+B)+18)
    #print(X//(A+B)-18)
    #print(X//(A+B)+19)
    #print(X//(A+B)-19)
    #print(X//(A+B)+20)
    #print(X//(A+B)-20)
    #print(X//(A+B)+21)
    #print(X//(A+B)-21)
    #print(X//(A+B)+22)
    #print(X//(A+B)-22)
    #print(X//(A+B)+23)
    #print(X//(A+B)-23

=======
Suggestion 9

def solve(a, b, x):
    # Write your code here
    return 0

=======
Suggestion 10

def digit(n):
    return len(str(n))
