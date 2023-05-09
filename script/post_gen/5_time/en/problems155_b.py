Synthesizing 5/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in a:
        if i % 2 == 0:
            if i % 3 != 0 and i % 5 != 0:
                print("DENIED")
                return
    print("APPROVED")

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i]%2 == 0:
            if a[i]%3 != 0 and a[i]%5 != 0:
                print("DENIED")
                return
    print("APPROVED")

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in a:
        if i%2 == 0 and i%3 != 0 and i%5 != 0:
            print("DENIED")
            exit()
    print("APPROVED")

=======
Suggestion 4

def check_divisibility_by_3_or_5(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            if arr[i] % 3 != 0 and arr[i] % 5 != 0:
                return "DENIED"
    return "APPROVED"

=======
Suggestion 5

def is_even(n):
    return n % 2 == 0
