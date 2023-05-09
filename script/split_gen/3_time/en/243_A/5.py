def main():
    V,A,B,C = map(int,input().split())
    if A > B:
        if B > C:
            print('M')
        else:
            print('T')
    else:
        if A > C:
            print('M')
        else:
            print('F')
