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
        print(":(")
    else:
        print("Yay!")

=======
Suggestion 3

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
Suggestion 4

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())

    if (e - a) <= k:
        print("Yay!")
    else:
        print(":(")

=======
Suggestion 5

def func():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())
    if (e - a) > k:
        print (":(")
    else:
        print ("Yay!")
func()

=======
Suggestion 6

def main():
    # get input
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())

    # check if antenna pair is greater than k
    if (b - a) > k:
        print(":(")
        return
    elif (c - a) > k:
        print(":(")
        return
    elif (d - a) > k:
        print(":(")
        return
    elif (e - a) > k:
        print(":(")
        return
    elif (c - b) > k:
        print(":(")
        return
    elif (d - b) > k:
        print(":(")
        return
    elif (e - b) > k:
        print(":(")
        return
    elif (d - c) > k:
        print(":(")
        return
    elif (e - c) > k:
        print(":(")
        return
    elif (e - d) > k:
        print(":(")
        return
    else:
        print("Yay!")
        return

main()
