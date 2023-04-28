Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = input()
    n = n.replace('1','x')
    n = n.replace('9','1')
    n = n.replace('x','9')
    print(n)

=======
Suggestion 2

def main():
    n = input()
    ans = ''
    for i in range(len(n)):
        if n[i] == '1':
            ans += '9'
        elif n[i] == '9':
            ans += '1'
    print(ans)

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
    n = input()
    print(n.replace('1', 'x').replace('9', '1').replace('x', '9'))

=======
Suggestion 5

def main():
    n = input()
    answer = ""
    for i in n:
        if i == "1":
            answer += "9"
        else:
            answer += "1"
    print(answer)

=======
Suggestion 6

def main():
    n = input()
    print(n.translate(str.maketrans({'1':'9','9':'1'})))

=======
Suggestion 7

def changeN(n):
    s = str(n)
    ans = ""
    for i in s:
        if i == "1":
            ans += "9"
        elif i == "9":
            ans += "1"
    return int(ans)
