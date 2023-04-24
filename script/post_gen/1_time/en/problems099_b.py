Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    print((b - a - 1) * (b - a) // 2 - a)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    print(((b - a) * (b - a + 1) // 2) - (b - a))

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    print((b-a)*(b-a+1)//2 - (b-a))

=======
Suggestion 4

def main():
    a,b = map(int,input().split())
    print((b*(b+1)//2)-(a*(a-1)//2)-b+a-1)

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    x = 0
    x = (b * (b + 1)) // 2 - (a * (a - 1)) // 2
    print(x - (b - a))

=======
Suggestion 6

def main():
    a,b=map(int,input().split())
    print(b-a-(b-a+1)*(b-a)//2)

main()

=======
Suggestion 7

def main():
    #write your code here
    a,b = map(int,input().split())
    print((b-a)*(b-a+1)//2-b)

=======
Suggestion 8

def get_snow_cover(a,b):
    #a = number of meters the west tower is not covered with snow
    #b = number of meters the east tower is not covered with snow
    #return number of meters the snow cover is deep
    return b - a - 1

=======
Suggestion 9

def get_sum(n):
    return n*(n+1)//2

=======
Suggestion 10

def snow_cover(a, b):
    print(b - a - 1)
