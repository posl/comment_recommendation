Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    print((b * (b + 1) // 2) - (a * (a - 1) // 2) - a)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    total = b * (b + 1) // 2 - a * (a - 1) // 2
    print(total - b + a - 1)

main()

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    print(b - a - int((b - a) * (b - a + 1) / 2))

=======
Suggestion 4

def main():
    a, b = [int(x) for x in input().split()]
    x = (b - a) * (b - a + 1) // 2 - b
    print(x)

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    print((b-a)*(b-a+1)//2 - b)

=======
Suggestion 6

def main():
    a,b = map(int,input().split())
    print((b-a)*(b-a+1)//2-b)

main()

=======
Suggestion 7

def main():
    a,b = map(int,input().split())
    print(b-a-(b-a)*(b-a+1)//2)

=======
Suggestion 8

def make_tower_list():
    tower_list = []
    for i in range(1, 1000):
        tower_list.append(i)
    return tower_list

=======
Suggestion 9

def snow_cover(a, b):
    # write your code here
    return 1
