Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())

    if e - a <= k:
        print("Yay!")
    else:
        print(":(")

=======
Suggestion 2

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())

    if e - a > k:
        print(':(')
    else:
        print('Yay!')

=======
Suggestion 3

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())
    if e - a <= k:
        print('Yay!')
    else:
        print(':(')

=======
Suggestion 4

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())
    if e - a > k:
        print(":(")
    else:
        print("Yay!")

=======
Suggestion 5

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())
    if (b - a) > k:
        print(":(")
        return
    if (c - b) > k:
        print(":(")
        return
    if (d - c) > k:
        print(":(")
        return
    if (e - d) > k:
        print(":(")
        return
    print("Yay!")

=======
Suggestion 6

def main():
    # input
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())

    # compute
    if e - a <= k:
        ans = 'Yay!'
    else:
        ans = ':('

    # output
    print(ans)

=======
Suggestion 7

def main():
    # input
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())
    # check
    if b - a > k:
        print(":(")
    elif c - a > k:
        print(":(")
    elif d - a > k:
        print(":(")
    elif e - a > k:
        print(":(")
    elif c - b > k:
        print(":(")
    elif d - b > k:
        print(":(")
    elif e - b > k:
        print(":(")
    elif d - c > k:
        print(":(")
    elif e - c > k:
        print(":(")
    elif e - d > k:
        print(":(")
    else:
        print("Yay!")
