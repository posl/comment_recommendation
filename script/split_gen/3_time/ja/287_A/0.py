def main():
    N = int(input())
    S = [input() for _ in range(N)]
    if S.count("For") > S.count("Against"):
        print("Yes")
    else:
        print("No")
