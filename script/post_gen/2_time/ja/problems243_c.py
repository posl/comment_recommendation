Synthesizing 1/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    XY = []
    for i in range(N):
        X, Y = map(int, input().split())
        XY.append((X, Y))
    S = input()
    #print(N)
    #print(XY)