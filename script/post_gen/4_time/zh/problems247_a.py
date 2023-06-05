Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    print(s[1:] + s[0])

=======
Suggestion 2

def main():
    s = input()
    ans = ''
    for i in range(4):
        if s[i] == '1':
            ans += '1'
        else:
            ans += '0'
    print(ans)

=======
Suggestion 3

def changeStatus(status):
    status = list(status)
    if status[0] == '1':
        status[0] = '0'
    else:
        status[0] = '1'
    return ''.join(status)

status = input()
print(changeStatus(status))

=======
Suggestion 4

def problems247_a():
    s = input()
    print(s[1:]+s[0])

=======
Suggestion 5

def main():
    S = input()
    #print(S)
    print(S[1:]+S[0])

=======
Suggestion 6

def main():
    S = input()
    print(S[1:] + S[0])
