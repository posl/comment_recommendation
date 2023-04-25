Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    r, D, x_2000 = map(int, input().split())
    for i in range(10):
        x = r * x_2000 - D
        print(x)
        x_2000 = x

=======
Suggestion 2

def main():
    r, D, x = map(int, input().split())
    for i in range(10):
        x = r * x - D
        print(x)

main()

=======
Suggestion 3

def main():
    r, D, x = map(int, input().split())
    for i in range(10):
        x = r * x - D
        print(x)

=======
Suggestion 4

def main():
    r, D, x_2000 = map(int, input().split())
    for i in range(10):
        x_2000 = r*x_2000 - D
        print(x_2000)

=======
Suggestion 5

def main():
    r, D, x = map(int, input().split())
    for i in range(10):
        x = r * x - D
        print(x)

main()

I tried to solve this problem with the following code. However, the code is not accepted. I don't know why. Could you help me?
