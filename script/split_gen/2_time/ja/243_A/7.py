def main():
    V,A,B,C = map(int,input().split())
    if V >= A and V >= B and V >= C:
        print('T')
    elif V >= A and V >= B and V < C:
        print('M')
    elif V >= A and V < B and V >= C:
        print('M')
    elif V >= A and V < B and V < C:
        print('F')
    elif V < A and V >= B and V >= C:
        print('M')
    elif V < A and V >= B and V < C:
        print('F')
    elif V < A and V < B and V >= C:
        print('F')
    elif V < A and V < B and V < C:
        print('F')
