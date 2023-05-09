def main():
    V, A, B, C = map(int, input().split())
    if A > B:
        if B > C:
            print("F")
        elif C > B:
            if V - A >= 0:
                print("T")
            else:
                print("F")
    elif B > A:
        if A > C:
            print("M")
        elif C > A:
            if V - B >= 0:
                print("T")
            else:
                print("M")
    elif A == B:
        if A > C:
            print("M")
        elif C > A:
            if V - A >= 0:
                print("T")
            else:
                print("M")
