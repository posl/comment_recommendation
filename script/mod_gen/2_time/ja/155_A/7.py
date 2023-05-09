def main():
    # A, B, C = map(int, input().split())
    A, B, C = map(int, input().split())
    if A == B:
        if B == C:
            print("No")
        else:
            print("Yes")
    elif B == C:
        print("Yes")
    elif A == C:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()