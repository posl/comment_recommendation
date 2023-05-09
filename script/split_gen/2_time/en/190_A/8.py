def main():
    A, B, C = map(int, input().split())
    if A > B:
        print("Takahashi")
    elif A < B:
        print("Aoki")
    elif A == B:
        if C == 0:
            print("Aoki")
        elif C == 1:
            print("Takahashi")
