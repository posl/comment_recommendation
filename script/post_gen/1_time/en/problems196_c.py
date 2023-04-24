Synthesizing 8/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if len(str(i)) % 2 == 0:
            if str(i)[:len(str(i))//2] == str(i)[len(str(i))//2:]:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        if len(str(i)) % 2 == 0:
            if str(i)[:int(len(str(i))/2)] == str(i)[int(len(str(i))/2):]:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if len(str(i)) % 2 == 0:
            if str(i)[0:int(len(str(i))/2)] == str(i)[int(len(str(i))/2):len(str(i))]:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        if len(str(i)) % 2 == 0:
            s = str(i)
            if s[:len(s) // 2] == s[len(s) // 2:]:
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    if n < 11:
        print(0)
    elif n < 111:
        print(9)
    elif n < 1111:
        print(9 + 10)
    elif n < 11111:
        print(9 + 10 + 100)
    elif n < 111111:
        print(9 + 10 + 100 + 1000)
    elif n < 1111111:
        print(9 + 10 + 100 + 1000 + 10000)
    elif n < 11111111:
        print(9 + 10 + 100 + 1000 + 10000 + 100000)
    elif n < 111111111:
        print(9 + 10 + 100 + 1000 + 10000 + 100000 + 1000000)
    elif n < 1111111111:
        print(9 + 10 + 100 + 1000 + 10000 + 100000 + 1000000 + 10000000)
    elif n < 11111111111:
        print(9 + 10 + 100 + 1000 + 10000 + 100000 + 1000000 + 10000000 + 100000000)
    else:
        print(9 + 10 + 100 + 1000 + 10000 + 100000 + 1000000 + 10000000 + 100000000 + 1000000000)

=======
Suggestion 6

def  main():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        s = str(i)
        if len(s) % 2 == 0 and s[:len(s)//2] == s[len(s)//2:]:
            ans += 1
    print(ans)

=======
Suggestion 7

def   f ( n ): 
     if   n   ==   0 : 
         return   1 
     return   9   *   10   **   ( n   //   2   -   1 )
