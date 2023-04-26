Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = input()
    n = n.replace('1', 'x')
    n = n.replace('9', '1')
    n = n.replace('x', '9')
    print(n)

=======
Suggestion 2

def main():
    n = input()
    n = n.replace('1', 'a')
    n = n.replace('9', '1')
    n = n.replace('a', '9')
    print(n)

=======
Suggestion 3

def main():
    n = input()
    n = n.replace("1","x")
    n = n.replace("9","1")
    n = n.replace("x","9")
    print(n)

=======
Suggestion 4

def main():
    # input
    N = input()
    # compute
    ans = ''
    for n in N:
        if n == '1':
            ans += '9'
        elif n == '9':
            ans += '1'
        else:
            ans += n
    # output
    print(ans)

=======
Suggestion 5

def main():
    n = input()
    print(n.replace('1','x').replace('9','1').replace('x','9'))

=======
Suggestion 6

def main():
    n = int(input())
    print(str(n)[::-1].replace('1', '2').replace('9', '1').replace('2', '9'))
