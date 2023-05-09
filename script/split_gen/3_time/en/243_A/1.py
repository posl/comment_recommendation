def main():
    V, A, B, C = map(int, input().split())
    if V < A:
        print('F')
    elif V < B:
        print('M')
    elif V < C:
        print('T')
    else:
        if A < B:
            if A < C:
                print('F')
            else:
                print('T')
        else:
            if B < C:
                print('M')
            else:
                print('T')
