def main():
    V, A, B, C = map(int, input().split())
    if V <= A:
        print("T")
    elif V <= A + B:
        print("M")
    elif V <= A + B + C:
        print("F")
    elif A + B + C < V:
        print("M")
main()
