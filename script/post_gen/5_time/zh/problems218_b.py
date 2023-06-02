Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    line = input()
    line = line.split()
    for i in range(len(line)):
        line[i] = int(line[i])
    for i in range(len(line)):
        line[i] -= 1
    output = [0 for i in range(len(line))]
    for i in range(len(line)):
        output[line[i]] = chr(ord('a') + i)
    print(''.join(output))

=======
Suggestion 2

def main():
    p = list(map(int, input().split()))
    s = ''
    for i in range(26):
        s += chr(ord('a') + p[i] - 1)
    print(s)

=======
Suggestion 3

def main():
    a = input()
    b = a.split()
    c = []
    for i in b:
        c.append(chr(int(i)+96))
    print(''.join(c))

=======
Suggestion 4

def main():
    p = list(map(int, input().split()))
    s = [chr(ord('a') + i - 1) for i in p]
    print(''.join(s))

=======
Suggestion 5

def main():
    p = list(map(int, input().split()))
    s = ''
    for i in p:
        s += chr(ord('a') + i - 1)
    print(s)

=======
Suggestion 6

def main():
    P = input().split(' ')
    P = [int(i) for i in P]
    S = [0]*26
    for i in range(26):
        S[P[i]-1] = chr(i+97)
    print(''.join(S))

=======
Suggestion 7

def main():
    p = list(map(int, input().split()))
    s = [chr(ord('a') + p[i] - 1) for i in range(len(p))]
    print(''.join(s))

=======
Suggestion 8

def main():
    p = list(map(int, input().split()))
    s = [chr(p[i] + 96) for i in range(26)]
    print(''.join(s))

=======
Suggestion 9

def main():
    p = input()
    p = p.split()
    s = ''
    for i in p:
        s += chr(int(i) + 96)
    print(s)
