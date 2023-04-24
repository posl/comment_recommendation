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
    n = list(n)
    for i in range(len(n)):
        if n[i] == '1':
            n[i] = '9'
        elif n[i] == '9':
            n[i] = '1'
    n = ''.join(n)
    print(n)

main()

=======
Suggestion 3

def main():
    n = input()
    n = n.replace("1","2")
    n = n.replace("9","1")
    n = n.replace("2","9")
    print(n)

=======
Suggestion 4

def main():
    n = input()
    print(n.replace('1', 'a').replace('9', '1').replace('a', '9'))

=======
Suggestion 5

def main():
    n = input()
    n = n.replace("1","9")
    n = n.replace("9","1")
    print(n)

=======
Suggestion 6

def main():
    n = input()
    print(n.replace("1","a").replace("9","1").replace("a","9"))

=======
Suggestion 7

def main():
    n = str(input())
    n = n.replace('1','9')
    n = n.replace('9','1')
    print(n)

=======
Suggestion 8

def main():
    n = int(input())
    print(n // 100)
    print(n % 100 // 10)
    print(n % 10)
    print(n % 100 % 10)

    print(n % 10 * 100 + n % 100 // 10 * 10 + n // 100)
