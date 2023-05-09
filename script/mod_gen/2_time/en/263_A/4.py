def is_full_house(A,B,C,D,E):
    if A==B and B==C:
        if D==E:
            return True
    if A==B and B==D:
        if C==E:
            return True
    if A==B and B==E:
        if C==D:
            return True
    if A==C and C==D:
        if B==E:
            return True
    if A==C and C==E:
        if B==D:
            return True
    if A==D and D==E:
        if B==C:
            return True
    if B==C and C==D:
        if A==E:
            return True
    if B==C and C==E:
        if A==D:
            return True
    if B==D and D==E:
        if A==C:
            return True
    if C==D and D==E:
        if A==B:
            return True
    return False
A,B,C,D,E = map(int,input().split())

if __name__ == '__main__':
    is_full_house()