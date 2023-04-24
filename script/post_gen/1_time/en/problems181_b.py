Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        a, b = map(int, input().split())
        sum += (b - a + 1) * (a + b) / 2
    print(int(sum))

=======
Suggestion 2

def main():
    n = int(input())
    total = 0
    for _ in range(n):
        a, b = map(int, input().split())
        total += (a + b) * (b - a + 1) // 2
    print(total)

=======
Suggestion 3

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    print(sum(b) - sum(a) + n)

=======
Suggestion 4

def main():
    # Get input
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)

    # Calculate the sum of the integers written
    sum = 0
    for i in range(n):
        sum += (b[i] - a[i] + 1) * (a[i] + b[i]) / 2

    # Print the sum of the integers written
    print(int(sum))

=======
Suggestion 5

def sum_natural_numbers(n):
    return (n*(n+1))//2

n = int(input())
sum = 0
for i in range(n):
    a,b = map(int,input().split())
    sum += sum_natural_numbers(b) - sum_natural_numbers(a-1)
print(sum)

=======
Suggestion 6

def getSumOfIntegersWrittenOnBlackboard():
    N = int(input())
    sum = 0
    for i in range(N):
        A, B = map(int, input().split())
        sum += (B - A + 1) * (A + B) / 2
    print(int(sum))

getSumOfIntegersWrittenOnBlackboard()

=======
Suggestion 7

def sum_of_arithmetic_progression(first_term, last_term, number_of_terms):
    sum = ((first_term + last_term) * number_of_terms) / 2
    return sum

=======
Suggestion 8

def sum_of_all_nums(start_num, end_num):
    return (start_num + end_num) * (end_num - start_num + 1) // 2

=======
Suggestion 9

def calc(n, a):
    return int((n * (n + 1)) / 2) - int((a * (a + 1)) / 2)
