Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, c, d, e = map(int, input().split())
    ans = len(set([a, b, c, d, e]))
    print(ans)

=======
Suggestion 2

def distinct_integers(a, b, c, d, e):
    return len(set([a, b, c, d, e]))

=======
Suggestion 3

def distinct_integers(a,b,c,d,e):
    distinct_list = []
    for i in [a,b,c,d,e]:
        if i not in distinct_list:
            distinct_list.append(i)
    return len(distinct_list)

=======
Suggestion 4

def main():
    a,b,c,d,e = map(int, input().split())
    print(len(set([a,b,c,d,e])))

=======
Suggestion 5

def problem_statement():
    #print how many distinct integers there are in given five integers A, B, C, D, and E.
    #Constraints
    #0 ≦ A, B, C, D, E ≦ 100
    #All values in input are integers.
    #
    #Input
    #Input is given from Standard Input in the following format:
    #A B C D E
    #
    #Output
    #Print the answer.
    #
    #Sample Input 1
    #31 9 24 31 24
    #
    #Sample Output 1
    #3
    #In the given five integers 31, 9, 24, 31, and 24, there are three distinct integers 9, 24, and 31.
    #Thus, 3 should be printed.
    #
    #Sample Input 2
    #0 0 0 0 0
    #
    #Sample Output 2
    #1
    pass

=======
Suggestion 6

def main():
    input_line = input()
    input_list = input_line.split()
    input_list = list(map(int, input_list))
    input_list.sort()
    distinct_count = 1
    for i in range(len(input_list)-1):
        if input_list[i] != input_list[i+1]:
            distinct_count += 1
    print(distinct_count)

=======
Suggestion 7

def main():
    # Take input
    a = input()
    b = input()
    c = input()
    d = input()
    e = input()
    # Calculate and print result
    print(len(set([a, b, c, d, e])))

=======
Suggestion 8

def main():
    x = input()
    x = x.split()
    x = [int(x) for x in x]
    x = set(x)
    print(len(x))

=======
Suggestion 9

def main():
    a = input().split()
    a = list(dict.fromkeys(a))
    print(len(a))

=======
Suggestion 10

def main():
    a = input().split()
    print(len(set(a)))
