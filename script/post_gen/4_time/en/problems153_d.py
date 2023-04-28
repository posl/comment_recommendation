Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    h = int(input())
    count = 0
    while h > 0:
        count += 2 ** (h.bit_length() - 1)
        h -= 2 ** (h.bit_length() - 1)
    print(count)

=======
Suggestion 2

def main():
    h = int(input())
    count = 0
    while h > 0:
        count += 1
        h = h // 2
    print(2**count - 1)

=======
Suggestion 3

def solution(H):
    if H == 1:
        return 1
    else:
        return 2*solution(H//2)+1

H = int(input())
print(solution(H))

=======
Suggestion 4

def main():
    H = int(input())
    counter = 0
    while H > 0:
        H = H // 2
        counter = counter + 1
    print(2**counter - 1)

=======
Suggestion 5

def main():
    h = int(input())
    print(2**(h.bit_length())-1)

=======
Suggestion 6

def main():
    H = int(input())
    print(2**(H.bit_length())-1)

=======
Suggestion 7

def main():
    H = int(input())
    print(2**(H.bit_length())-1)
    return
