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
    n = int(input())
    n = str(n)
    n = n.replace('1', '2')
    n = n.replace('9', '1')
    n = n.replace('2', '9')
    print(n)

=======
Suggestion 4

def main():
    n = input()
    print(n.replace('1', 'x').replace('9', '1').replace('x', '9'))
main()

=======
Suggestion 5

def main():
    n = input()
    print(n.replace('1','x').replace('9','1').replace('x','9'))

=======
Suggestion 6

def main():
    n = input()
    print(n.replace('1','X').replace('9','1').replace('X','9'))

=======
Suggestion 7

def main():
    n = int(input())
    n = str(n)
    print(n.replace('9', 'x').replace('1', '9').replace('x', '1'))

=======
Suggestion 8

def main():
    num = input()
    print(num.replace('1', '9').replace('9', '1').replace('9', '9'))
main()

=======
Suggestion 9

def main():
    n = input("Enter a 3 digit number: ")
    if n.isdigit():
        if len(n) == 3:
            if n[0] == '1' and n[1] == '1' and n[2] == '9':
                print("991")
            elif n[0] == '9' and n[1] == '1' and n[2] == '1':
                print("111")
            elif n[0] == '9' and n[1] == '1' and n[2] == '9':
                print("111")
            elif n[0] == '1' and n[1] == '9' and n[2] == '9':
                print("919")
            elif n[0] == '1' and n[1] == '9' and n[2] == '1':
                print("919")
            elif n[0] == '9' and n[1] == '9' and n[2] == '1':
                print("191")
            elif n[0] == '9' and n[1] == '9' and n[2] == '9':
                print("111")
            elif n[0] == '1' and n[1] == '9' and n[2] == '9':
                print("919")
            elif n[0] == '1' and n[1] == '1' and n[2] == '1':
                print("999")
        else:
            print("Please enter a 3 digit number")
    else:
        print("Please enter a 3 digit number")
