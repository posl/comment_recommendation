def main():
    # Read input
    V, A, B, C = map(int, input().split())
    # Solve the problem
    if V < A:
        print("T")
    elif V < A + B:
        print("F")
    elif V < A + B + C:
        print("M")
    else:
        print("T")
