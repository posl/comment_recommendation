Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    print(max(c - (a - b), 0))

=======
Suggestion 2

def problem136_a():
    a, b, c = map(int, input().split())
    print(max(c - (a - b), 0))

=======
Suggestion 3

def main():
    # Get input here
    a, b, c = map(int, input().strip().split())
    
    # Calculate result here
    result = max(c - (a - b), 0)
    
    # Print output here
    print(result)

main()

=======
Suggestion 4

def main():
    a,b,c = map(int, input().split())
    print(max(0, c-(a-b)))

=======
Suggestion 5

def main():
    A = int(input())
    B = int(input())
    C = int(input())

    if A >= B:
        print(A - B)
    else:
        print(0)

=======
Suggestion 6

def water_transfer(a,b,c):
    if a >= b:
        if a >= b + c:
            return 0
        else:
            return b + c - a
    else:
        return c

=======
Suggestion 7

def calc_water(a, b, c):
    return c - (a - b)

=======
Suggestion 8

def water_remain(A,B,C):
    return C - (A - B)
