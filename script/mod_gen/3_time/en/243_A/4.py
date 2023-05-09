def main():
    V, A, B, C = map(int, input().split())
    if V == A:
        print("T")
    elif V == B:
        print("M")
    elif V == C:
        print("F")
    elif A > B and A > C:
        print("F")
    elif B > A and B > C:
        print("T")
    else:
        print("M")

if __name__ == '__main__':
    main()