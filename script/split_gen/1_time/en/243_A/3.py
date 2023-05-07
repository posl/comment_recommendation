def main():
    V, A, B, C = [int(x) for x in input().split()]
    if V < A:
        print("F")
    elif V < B:
        print("M")
    elif V < C:
        print("T")
    else:
        print("M")
