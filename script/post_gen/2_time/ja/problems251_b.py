Synthesizing 1/10 solutions

=======
Suggestion 1

def main():
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    # print(n, w, a)

    # おもりが3個以下の場合は、全探索でOK
    if n <= 3:
