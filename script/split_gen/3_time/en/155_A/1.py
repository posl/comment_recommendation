def main():
    A, B, C = map(int, input().split())
    if (A == B and A != C) or (A == C and A != B) or (B == C and B != A):
        print("Yes")
    else:
        print("No")
