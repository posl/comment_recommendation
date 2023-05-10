Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(float, input().split())
    print(int(a * b))

=======
Suggestion 2

def main():
    a,b = map(float,input().split())
    print(int(a*b//1))

=======
Suggestion 3

def main():
    a,b = map(float,input().split())
    ans = int(a*b)
    print(ans)

=======
Suggestion 4

def main():
    a, b = input().split()
    a = int(a)
    b = int(b.replace('.', ''))
    print(a * b // 100)

=======
Suggestion 5

def main():
    a,b = map(float,input().split())
    print(int(a*b))
main()

=======
Suggestion 6

def main():
    a, b = map(str, input().split())
    a = int(a)
    b = int(float(b)*100)
    print(a*b//100)
