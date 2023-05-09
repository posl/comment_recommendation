def main():
    V, A, B, C = map(int, input().split())
    if A > B:
        A, B = B, A
    if A > C:
        A, C = C, A
    if B > C:
        B, C = C, B
    if A > V:
        print("F")
    elif B > V:
        print("M")
    else:
        print("T")
