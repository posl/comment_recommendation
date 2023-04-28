Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a = list(map(int, input().split()))
    b = a[0]
    for i in range(3):
        b = a[b]
    print(b)

=======
Suggestion 2

def main():
    a = [int(i) for i in input().split()]
    n = 0
    for i in range(3):
        n = a[n]
    print(n)

=======
Suggestion 3

def main():
    a = list(map(int, input().split()))
    b = []
    b.append(0)
    b.append(a[0])
    b.append(a[a[0]])
    b.append(a[a[a[0]]])
    b.append(a[a[a[a[0]]]])
    b.append(a[a[a[a[a[0]]]]])
    b.append(a[a[a[a[a[a[0]]]]]])
    b.append(a[a[a[a[a[a[a[0]]]]]]])
    b.append(a[a[a[a[a[a[a[a[0]]]]]]]])
    b.append(a[a[a[a[a[a[a[a[a[0]]]]]]]]])
    print(b[3])

=======
Suggestion 4

def main():
    a = input().split()
    b = 0
    for i in range(3):
        b = int(a[b])
    print(b)

=======
Suggestion 5

def main():
    #input
    a = list(map(int, input().split()))
    #compute
    for i in range(3):
        a = [a[a[i]] for i in range(10)]
    #output
    print(a[0])

=======
Suggestion 6

def main():
    # input
    a = list(map(int, input().split()))

    # compute

    # output
    print(a[3])

=======
Suggestion 7

def calc(a):
    i = 0
    while i < 3:
        a = a[a[i]]
        i += 1
    return a

=======
Suggestion 8

def main():
    a = list(map(int, input().split()))
    print(a[0])
    return

=======
Suggestion 9

def get_input():
    input_line = input()
    input_list = input_line.split()
    return input_list

=======
Suggestion 10

def get_input():
    return list(map(int, input().split()))
