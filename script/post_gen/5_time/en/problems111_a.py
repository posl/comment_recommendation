Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = input()
    n = n.replace("1", "x")
    n = n.replace("9", "1")
    n = n.replace("x", "9")
    print(n)

=======
Suggestion 2

def main():
    n = input()
    n = n.replace('1','a')
    n = n.replace('9','1')
    n = n.replace('a','9')
    print(n)

=======
Suggestion 3

def main():
    n = input()
    print(n.replace('1', '2').replace('9', '1').replace('2', '9'))

=======
Suggestion 4

def main():
    n = input()
    print(n.replace('1','a').replace('9','1').replace('a','9'))

=======
Suggestion 5

def main():
    n = input()
    print(n.replace('9','a').replace('1','9').replace('a','1'))

=======
Suggestion 6

def main():
    n = input()
    print(n.translate(str.maketrans('19', '91')))

=======
Suggestion 7

def replace_1_9(n):
    n = str(n)
    result = ''
    for i in range(0, len(n)):
        if n[i] == '1':
            result = result + '9'
        elif n[i] == '9':
            result = result + '1'
    return result

n = input()
print(replace_1_9(n))

=======
Suggestion 8

def main():
    #n = int(input())
    n = 999
    print(n)
    #print(111)
    #print(999)
    #print(100)
    #print(999)
    #print(111)
    #print(199)
    #prin
