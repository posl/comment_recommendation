def main():
    S = input()
    if "a" in S:
        print(len(S) - S[::-1].index("a"))
    else:
        print(-1)
