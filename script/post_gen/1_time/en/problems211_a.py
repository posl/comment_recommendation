Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    C = (A - B) / 3 + B
    print(C)

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    C = ((A-B)/(3)) +B
    print(C)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    print((a - b) / 3 + b)

=======
Suggestion 4

def main():
    A,B = [int(x) for x in input().split()]
    C = ((A-B)/3) + B
    print(C)

=======
Suggestion 5

def main():
    line = input().split()
    A = int(line[0])
    B = int(line[1])

    C = ((A-B)/3) + B
    print(C)

main()

=======
Suggestion 6

def main():
    A, B = map(int,input().split())
    C = ((A-B)/3) + B
    print(C)

=======
Suggestion 7

def main():
    # Read input
    A, B = map(int, input().split())

    # Calculate mean arterial pressure
    C = ((A - B) / 3) + B

    # Print output
    print(C)

=======
Suggestion 8

def mean_arterial_pressure(systolic, diastolic):
    return (systolic - diastolic) / 3 + diastolic

=======
Suggestion 9

def main():
    A,B = map(int,input().split())
    print((A-B)/3+B)

=======
Suggestion 10

def get_input():
    return list(map(int, input().split()))
