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
    new_n = ""
    for i in n:
        if i == "9":
            new_n += "1"
        else:
            new_n += "9"
    print(new_n)

main()

=======
Suggestion 3

def main():
    n = int(input())
    x = str(n)
    x = x.replace('9', 'x')
    x = x.replace('1', '9')
    x = x.replace('x', '1')
    print(x)

main()

=======
Suggestion 4

def main():
    n = input()
    n = n.replace('1', '9')
    n = n.replace('9', '1')
    print(n)

=======
Suggestion 5

def main():
    n = input()
    print(n.replace("1", "t").replace("9", "1").replace("t", "9"))

=======
Suggestion 6

def reverse(n):
    n = str(n)
    n = n.replace("9", "x")
    n = n.replace("1", "9")
    n = n.replace("x", "1")
    return n

=======
Suggestion 7

def main():
    n = input()
    print(n.replace('1','x').replace('9','1').replace('x','9'))

=======
Suggestion 8

def flip(n):
    return int(str(n).translate(str.maketrans('19', '91')))

=======
Suggestion 9

def flip(n):
    return str(1110 - n)

print(flip(int(input())))
