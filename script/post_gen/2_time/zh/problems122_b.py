Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    b = input()
    if b == 'A':
        print('T')
    elif b == 'C':
        print('G')
    elif b == 'G':
        print('C')
    elif b == 'T':
        print('A')

=======
Suggestion 2

def main():
    b = input()
    if b == 'A':
        print('T')
    elif b == 'T':
        print('A')
    elif b == 'C':
        print('G')
    elif b == 'G':
        print('C')

=======
Suggestion 3

def get_complementary_base(base):
    if base == 'A':
        return 'T'
    if base == 'T':
        return 'A'
    if base == 'C':
        return 'G'
    if base == 'G':
        return 'C'

base = input()
print(get_complementary_base(base))

=======
Suggestion 4

def main():
    b = input()
    if b == "A":
        print("T")
    elif b == "T":
        print("A")
    elif b == "C":
        print("G")
    elif b == "G":
        print("C")

=======
Suggestion 5

def main():
    b = input()
    if b == 'A':
        print('T')
    elif b == 'T':
        print('A')
    elif b == 'G':
        print('C')
    elif b == 'C':
        print('G')
    else:
        print('输入错误')

=======
Suggestion 6

def main():
    b=input()
    if b=='A':
        print('T')
    elif b=='T':
        print('A')
    elif b=='C':
        print('G')
    elif b=='G':
        print('C')
    else:
        print('输入有误')
