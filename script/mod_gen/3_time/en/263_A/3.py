def main():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    A, B, C, D, E = map(int, input().split())
    if (A == B == C) and (D == E) or (A == B) and (C == D == E):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()