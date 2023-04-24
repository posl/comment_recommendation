Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    abc = input()
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    print(a+b+c)

=======
Suggestion 2

def main():
    a = input()
    b = a[1] + a[2] + a[0]
    c = a[2] + a[0] + a[1]
    print(int(a) + int(b) + int(c))

=======
Suggestion 3

def main():
    abc = int(input())
    a = abc // 100
    b = (abc - a * 100) // 10
    c = abc - a * 100 - b * 10
    print(a + b + c)

=======
Suggestion 4

def main():
    abc = input()
    print(int(abc[0]) + int(abc[1]) + int(abc[2]))

=======
Suggestion 5

def main():
    #input
    abc = int(input())
    #compute
    bca = abc % 100 * 10 + abc // 100
    cab = abc % 10 * 100 + abc // 10
    #output
    print(abc + bca + cab)

=======
Suggestion 6

def main():
    S = input()
    print(int(S[0])+int(S[1])+int(S[2]))

=======
Suggestion 7

def main():
    # a = input()
    a = "123"
    print(int(a[0]) + int(a[1]) + int(a[2]))

=======
Suggestion 8

def main():
    # your code here
    a = input()
    b = a[::-1]
    print(int(a)+int(b))

=======
Suggestion 9

def main():
    a = int(input())
    print(a*2)
