Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    ans = ""
    cnt = 0
    for i in range(n):
        if s[i] == '"':
            cnt += 1
            if cnt % 2 == 1:
                ans += '"'
            else:
                ans += '.'
        else:
            ans += s[i]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    ans = ""
    count = 0
    for i in range(N):
        if S[i] == '"':
            count += 1
        elif S[i] == ',' and count % 2 == 0:
            ans += '.'
        else:
            ans += S[i]
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    s = input()
    flag = False
    for i in range(n):
        if s[i] == '"':
            flag = not flag
        else:
            if flag:
                print(s[i],end='')
            else:
                print('.',end='')
    print('')

=======
Suggestion 4

def main():
    n = int(input())
    s = input()
    s = list(s)
    for i in range(n):
        if s[i] == '"':
            if s[i+1] == '"':
                s[i] = '.'
                s[i+1] = '.'
    print(''.join(s))

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    S = S.replace('"', '')
    S = S.replace(',', '.')
    print(S)

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    queue = []
    for i in range(N):
        if S[i] == '"':
            queue.append(i)
        elif len(queue) % 2 == 0:
            S = S[:i] + '.' + S[i+1:]
    print(S)

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    S = S.replace("\"", "")
    S = S.replace(",", ".")
    print(S)

main()

=======
Suggestion 8

def main():
    N = input()
    S = input()
    S = S.replace('"', '')
    S = S.replace(',', '.')
    print(S)

=======
Suggestion 9

def main():
    N = int(input())
    S = input()
    S = S.replace(",", ".")
    S = S.replace('"', "")
    print(S)

=======
Suggestion 10

def replace_comma(str):
    count = 0
    new_str = ""
    for i in str:
        if i == '"':
            count += 1
        elif i == ',' and count % 2 == 0:
            new_str += '.'
        else:
            new_str += i
    return new_str
