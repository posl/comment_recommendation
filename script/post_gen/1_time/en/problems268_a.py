Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, C, D, E = map(int, input().split())
    print(len(set([A, B, C, D, E])))

=======
Suggestion 2

def main():
    #input
    a, b, c, d, e = map(int, input().split())
    #output
    print(len(set([a, b, c, d, e])))

=======
Suggestion 3

def main():
    a = list(map(int, input().split()))
    print(len(set(a)))

=======
Suggestion 4

def main():
    # read input
    A, B, C, D, E = map(int, input().split())
    # make set
    s = set()
    s.add(A)
    s.add(B)
    s.add(C)
    s.add(D)
    s.add(E)
    # print result
    print(len(s))

=======
Suggestion 5

def main():
    # 1. Input
    a, b, c, d, e = map(int, input().split())
    # 2. Process
    # 3. Output
    print(len(set([a, b, c, d, e])))

=======
Suggestion 6

def main():
    A = list(map(int, input().split()))
    print(len(set(A)))

=======
Suggestion 7

def main():
    inputList = input().split()
    inputSet = set(inputList)
    print(len(inputSet))

=======
Suggestion 8

def main():
    numbers = input().split()
    print(len(set(numbers)))

=======
Suggestion 9

def main():
    input_list = input().split()
    print(len(set(input_list)))

=======
Suggestion 10

def main():
    #Read input
    input_list = input().split()
    #Convert input to integers
    int_list = [int(i) for i in input_list]
    #Convert to set to remove duplicates
    int_set = set(int_list)
    #Print length of set
    print(len(int_set))
