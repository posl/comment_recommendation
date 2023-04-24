Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = [int(x) for x in input().split()]
    for i in range(5):
        if x[i] == 0:
            print(i+1)
            break

=======
Suggestion 2

def main():
    x1, x2, x3, x4, x5 = map(int, input().split())
    print(x1.index(0) + 1)

main()

=======
Suggestion 3

def main():
    x = list(map(int, input().split()))
    print(x.index(0) + 1)

=======
Suggestion 4

def main():
    x1, x2, x3, x4, x5 = map(int, input().split())
    print(x1.index(0) + 1)

=======
Suggestion 5

def main():
    x = map(int, raw_input().split())
    for i in range(0, len(x)):
        if x[i] == 0:
            print i + 1
            break

main()

=======
Suggestion 6

def main():
    #input
    x_1, x_2, x_3, x_4, x_5 = map(int, input().split())
    #output
    if x_1 == 0:
        print(1)
    elif x_2 == 0:
        print(2)
    elif x_3 == 0:
        print(3)
    elif x_4 == 0:
        print(4)
    else:
        print(5)

=======
Suggestion 7

def main():
    input_list = [int(i) for i in input().split()]
    for i in range(5):
        if input_list[i] == 0:
            print(i+1)
            break
