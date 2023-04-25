Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    for c in s:
        print(chr((ord(c) - ord('A') + n) % 26 + ord('A')), end='')
    print()

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    print(''.join([chr((ord(c) - ord('A') + n) % 26 + ord('A')) for c in s]))

=======
Suggestion 3

def main():
    n = int(input())
    s = input()
    for c in s:
        if ord(c) + n > ord('Z'):
            print(chr(ord(c) + n - 26), end='')
        else:
            print(chr(ord(c) + n), end='')

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    for s in S:
        if s == "Z":
            print("A", end="")
        elif s == "Y":
            print("B", end="")
        elif s == "X":
            print("C", end="")
        elif s == "W":
            print("D", end="")
        elif s == "V":
            print("E", end="")
        elif s == "U":
            print("F", end="")
        elif s == "T":
            print("G", end="")
        elif s == "S":
            print("H", end="")
        elif s == "R":
            print("I", end="")
        elif s == "Q":
            print("J", end="")
        elif s == "P":
            print("K", end="")
        elif s == "O":
            print("L", end="")
        elif s == "N":
            print("M", end="")
        elif s == "M":
            print("N", end="")
        elif s == "L":
            print("O", end="")
        elif s == "K":
            print("P", end="")
        elif s == "J":
            print("Q", end="")
        elif s == "I":
            print("R", end="")
        elif s == "H":
            print("S", end="")
        elif s == "G":
            print("T", end="")
        elif s == "F":
            print("U", end="")
        elif s == "E":
            print("V", end="")
        elif s == "D":
            print("W", end="")
        elif s == "C":
            print("X", end="")
        elif s == "B":
            print("Y", end="")
        elif s == "A":
            print("Z", end="")
        else:
            print(chr(ord(s)+N), end="")
    print()

=======
Suggestion 5

def shift(s, n):
    for i in range(len(s)):
        if ord(s[i]) + n > 90:
            s = s[:i] + chr(ord(s[i]) + n - 26) + s[i+1:]
        else:
            s = s[:i] + chr(ord(s[i]) + n) + s[i+1:]
    return s

n = int(input())
s = input()
print(shift(s, n))

=======
Suggestion 6

def main():
    n = int(input())
    s = input()
    for i in s:
        print(chr((ord(i)-65+n)%26+65), end='')

=======
Suggestion 7

def shift(s,n):
    s = list(s)
    for i in range(len(s)):
        if s[i] != ' ':
            s[i] = chr(((ord(s[i]) - 65 + n) % 26) + 65)
    return ''.join(s)

=======
Suggestion 8

def shift(s, n):
    #convert string to list
    s = list(s)
    #convert each letter to its ascii code
    for i in range(len(s)):
        s[i] = ord(s[i])
    #add n to each ascii code
    for i in range(len(s)):
        s[i] = s[i] + n
    #convert each ascii code to its letter
    for i in range(len(s)):
        s[i] = chr(s[i])
    #convert list to string
    s = ''.join(s)
    return s
