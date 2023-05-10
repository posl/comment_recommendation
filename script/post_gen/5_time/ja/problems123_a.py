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
    if e - a > k:
        print(':(')
    else:
        print('Yay!')

=======
Suggestion 2

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())

    if (b - a) > k:
        print(':(')
    elif (c - b) > k:
        print(':(')
    elif (d - c) > k:
        print(':(')
    elif (e - d) > k:
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

    if (b-a) > k:
        print(":(")
        return
    if (c-a) > k:
        print(":(")
        return
    if (d-a) > k:
        print(":(")
        return
    if (e-a) > k:
        print(":(")
        return
    if (c-b) > k:
        print(":(")
        return
    if (d-b) > k:
        print(":(")
        return
    if (e-b) > k:
        print(":(")
        return
    if (d-c) > k:
        print(":(")
        return
    if (e-c) > k:
        print(":(")
        return
    if (e-d) > k:
        print(":(")
        return

    print("Yay!")

=======
Suggestion 4

def main():
    # a, b, c, d, e, k = map(int, input().split())
    # print("Yay!" if e-a <= k else ":(")
    a, b, c, d, e, k = [int(input()) for i in range(6)]
    print("Yay!" if e-a <= k else ":(")

=======
Suggestion 5

def main():
    #input
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())

    #compute
    if e - a <= k:
        print("Yay!")
    else:
        print(":(")

=======
Suggestion 6

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())
    if (b - a) > k:
        print(':(')
    elif (c - a) > k:
        print(':(')
    elif (d - a) > k:
        print(':(')
    elif (e - a) > k:
        print(':(')
    elif (c - b) > k:
        print(':(')
    elif (d - b) > k:
        print(':(')
    elif (e - b) > k:
        print(':(')
    elif (d - c) > k:
        print(':(')
    elif (e - c) > k:
        print(':(')
    elif (e - d) > k:
        print(':(')
    else:
        print('Yay!')

main()

=======
Suggestion 7

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
Suggestion 8

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())

    if (b - a) > k:
        print(":(")
    elif (c - a) > k:
        print(":(")
    elif (d - a) > k:
        print(":(")
    elif (e - a) > k:
        print(":(")
    elif (c - b) > k:
        print(":(")
    elif (d - b) > k:
        print(":(")
    elif (e - b) > k:
        print(":(")
    elif (d - c) > k:
        print(":(")
    elif (e - c) > k:
        print(":(")
    elif (e - d) > k:
        print(":(")
    else:
        print("Yay!")
