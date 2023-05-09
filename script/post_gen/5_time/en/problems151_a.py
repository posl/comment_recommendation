Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    c = input()
    print(chr(ord(c) + 1))

=======
Suggestion 2

def main():
    c = input()
    c = chr(ord(c) + 1)
    print(c)

=======
Suggestion 3

def main():
    C = input()
    print(chr(ord(C)+1))

=======
Suggestion 4

def get_next_letter(letter):
    letter = ord(letter)
    letter += 1
    return chr(letter)
