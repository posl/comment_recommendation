Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = input()
    print(n.translate(str.maketrans('19','91')))

=======
Suggestion 2

def main():
    # input
    n = input()
    # solve
    ans = n.replace('1', 'x').replace('9', '1').replace('x', '9')
    # output
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    print(n%10*100 + n//10%10*10 + n//100)

=======
Suggestion 4

def main():
    n = input()
    print(n.replace('1', 'a').replace('9', '1').replace('a', '9'))

=======
Suggestion 5

def main():
    n = input()
    print(n.replace("1","a").replace("9","1").replace("a","9"))

=======
Suggestion 6

def main():
    n = int(input())
    print(str(n).replace('1', 'x').replace('9', '1').replace('x', '9'))

=======
Suggestion 7

def main():
    n = input()
    n = n.replace('1', 'x')
    n = n.replace('9', '1')
    n = n.replace('x', '9')
    print(n)

=======
Suggestion 8

def main():
    n = input()
    n1 = n.replace("1", "x")
    n2 = n1.replace("9", "1")
    n3 = n2.replace("x", "9")
    print(n3)
