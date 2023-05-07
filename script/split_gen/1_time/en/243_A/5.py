def main():
    V, A, B, C = map(int, input().split())
    if A >= B:
        if B >= C:
            print("F")
        elif A >= C:
            print("M")
        else:
            print("T")
    else:
        if A >= C:
            print("M")
        elif B >= C:
            print("T")
        else:
            print("F")
