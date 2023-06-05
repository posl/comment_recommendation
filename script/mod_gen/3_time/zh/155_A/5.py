def main():
    A, B, C = map(int, input().split())
    if A == B and A != C:
        print("是")
    elif B == C and B != A:
        print("是")
    elif A == C and A != B:
        print("是")
    else:
        print("否")
    return

if __name__ == '__main__':
    main()