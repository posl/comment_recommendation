Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problem099_a():
    n = int(input())
    if n < 1000:
        print("ABC")
    else:
        print("ABD")

=======
Suggestion 2

def main():
    n = int(input())
    if n <= 999:
        print("ABC")
    else:
        print("ABD")

=======
Suggestion 3

def main():
    n = int(input())
    if n < 1000:
        print("ABC")
    else:
        print("ABD")

=======
Suggestion 4

def get_abc(n):
    if n <= 999:
        return 'ABC'
    else:
        return 'ABD'

=======
Suggestion 5

def get_ABCD(n):
    if n <= 999:
        return "ABC"
    else:
        return "ABD"
    
n = int(input())
print(get_ABCD(n))
