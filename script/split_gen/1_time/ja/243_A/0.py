def main():
    V, A, B, C = map(int, input().split())
    if V < A:
        print('F')
    elif V < A + B:
        print('M')
    elif V < A + B + C:
        print('T')
    else:
        print('F')
