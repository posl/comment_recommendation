Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print((S_x * G_y + G_x * S_y) / (S_y + G_y))

=======
Suggestion 2

def solve():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print((G_x * S_y + S_x * G_y) / (S_y + G_y))

=======
Suggestion 3

def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    if S_x == G_x:
        print(S_x)
    else:
        print((S_x * G_y + G_x * S_y) / (S_y + G_y))

main()

=======
Suggestion 4

def main():
    #input
    S_x,S_y,G_x,G_y = map(int,input().split())
    #calc
    ans = S_x - S_x * G_y / (G_y - S_y)
    #output
    print(ans)

=======
Suggestion 5

def main():
    # read the input
    S_x, S_y, G_x, G_y = map(int, input().split())
    # calculate the result
    result = S_x * G_y / (S_y + G_y)
    # print the result
    print(result)
