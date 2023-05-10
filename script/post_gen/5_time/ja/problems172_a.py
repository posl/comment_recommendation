Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a = int(input())
    print(a + a**2 + a**3)

=======
Suggestion 2

def calc(a):
    return a + a**2 + a**3

=======
Suggestion 3

def main():
    a = int(input())
    sum = 0
    for i in range(1,4):
        sum += pow(a,i)
    print(sum)
