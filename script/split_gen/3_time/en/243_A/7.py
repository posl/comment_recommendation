def main():
    V,A,B,C = map(int, input().split())
    if A >= B and B >= C:
        print('F')
    elif A <= B and B <= C:
        print('M')
    else:
        print('T')
