Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(b - c, d - a))

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(b-d, a-c, b-c, a-d))

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(b-d, c-a))

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(b - c, d - a))
main()

Python Solution

a, b = map(int, input().split())
c, d = map(int, input().split())
print(max(b - c, d - a))

I solved this problem using the max function. The max function returns the largest of its arguments. So, I passed the arguments b - c and d - a to the max function. The max function returns the largest of these two arguments.

I solved this problem using the max function. The max function returns the largest of its arguments. So, I passed the arguments b - c and d - a to the max function. The max function returns the largest of these two arguments.

I solved this problem using the max function. The max function returns the largest of its arguments. So, I passed the arguments b - c and d - a to the max function. The max function returns the largest of these two arguments.

I solved this problem using the max function. The max function returns the largest of its arguments. So, I passed the arguments b - c and d - a to the max function. The max function returns the largest of these two arguments.

I solved this problem using the max function. The max function returns the largest of its arguments. So, I passed the arguments b - c and d - a to the max function. The max function returns the largest of these two arguments.

I solved this problem using the max function. The max function returns the largest of its arguments. So, I passed the arguments b - c and d - a to the max function. The max function returns the largest of these two arguments.

I solved this problem using the max function. The max function returns the largest of its arguments. So, I passed the arguments b - c and d - a to the max function. The max function returns the largest of these two arguments.

I solved this problem using the max function. The max function returns the largest of its arguments. So, I passed the arguments b - c and d - a to the max function. The max function returns the largest of these two arguments.

I solved this problem using the max function. The max function returns the largest of its arguments. So, I passed the arguments b - c and d - a to the max function. The max function returns the

=======
Suggestion 5

def main():
    #Read input
    a,b = map(int,input().split())
    c,d = map(int,input().split())
    #Find max value of x-y
    max1 = max(b,d)
    min1 = min(a,c)
    print(max1-min1)

=======
Suggestion 6

def main():
    #taking input
    a,b = map(int,input().split())
    c,d = map(int,input().split())
    #finding max of x-y and y-x
    print(max(a-d,b-c))
