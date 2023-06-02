Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H,A = map(int,input().split())
    if H%A == 0:
        print(H//A)
    else:
        print(H//A+1)

=======
Suggestion 2

def attack(hp, at):
    if hp % at == 0:
        return hp // at
    else:
        return hp // at + 1

=======
Suggestion 3

def main():
    H, A = map(int, input().split())
    print((H + A - 1) // A)

=======
Suggestion 4

def get_input():
    h, a = map(int, input().split())
    return h, a

=======
Suggestion 5

def main():
    H, A = map(int, input().split())
    count = 0
    while H > 0:
        H -= A
        count += 1
    print(count)

=======
Suggestion 6

def get_input():
    input = raw_input()
    input = input.split(" ")
    input = [int(x) for x in input]
    return input

=======
Suggestion 7

def main():
    h,a = map(int,input().split())
    print((h+a-1)//a)
