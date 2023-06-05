Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def replace_num(n):
    n = str(n)
    n = n.replace("1","a")
    n = n.replace("9","1")
    n = n.replace("a","9")
    return n

=======
Suggestion 2

def get_input():
    input = raw_input()
    return int(input)

=======
Suggestion 3

def replace_1_9(n):
    if n < 111 or n > 999:
        return
    else:
        n1 = n // 100
        n2 = n % 100 // 10
        n3 = n % 10
        n1 = 9 if n1 == 1 else 1
        n2 = 9 if n2 == 1 else 1
        n3 = 9 if n3 == 1 else 1
        return n1 * 100 + n2 * 10 + n3

=======
Suggestion 4

def main():
    n = int(input())
    print(1110-n)

=======
Suggestion 5

def main():
    n = input()
    print(n.replace('1','9').replace('9','1'))

=======
Suggestion 6

def main():
    n = input()
    for i in range(len(n)):
        if n[i] == '1':
            print('9', end='')
        else:
            print('1', end='')
    print()

=======
Suggestion 7

def main():
    n = input()
    print(n.replace('1','2').replace('9','1').replace('2','9'))

=======
Suggestion 8

def replace(s):
    s = s.replace("1","a")
    s = s.replace("9","1")
    s = s.replace("a","9")
    return s
