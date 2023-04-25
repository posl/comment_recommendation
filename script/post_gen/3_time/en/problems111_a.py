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
    n = n.replace("1", "x")
    n = n.replace("9", "1")
    n = n.replace("x", "9")
    print(n)

=======
Suggestion 3

def main():
    n = input()
    n = list(n)
    for i in range(len(n)):
        if n[i] == '1':
            n[i] = '9'
        elif n[i] == '9':
            n[i] = '1'
    print(''.join(n))
main()

=======
Suggestion 4

def main():
    n = input()
    n = n.replace('1', 'a')
    n = n.replace('9', '1')
    n = n.replace('a', '9')
    print(n)

=======
Suggestion 5

def main():
    n = input()
    n = n.replace("1", "x")
    n = n.replace("9", "1")
    n = n.replace("x", "9")
    print(n)
    return

main()

=======
Suggestion 6

def main():
    n = int(input())
    n = str(n)
    x = ""
    for i in n:
        if i == "1":
            x += "9"
        elif i == "9":
            x += "1"
    print(x)

=======
Suggestion 7

def main():
    n = input()
    print(n.translate(str.maketrans('19', '91')))

=======
Suggestion 8

def main():
    # Read input
    n = input()
    # Replace 9 with 1 and 1 with 9
    n = n.replace('9', 'x')
    n = n.replace('1', '9')
    n = n.replace('x', '1')
    # Print output
    print(n)
