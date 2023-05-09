def main():
    A, B, C = map(int, input().split())
    if A == B or A == C or B == C:
        print("Yes")
    else:
        print("No")
