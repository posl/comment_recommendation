def main():
    A,B,C,D,E = map(int,input().split())
    if A==B==C:
        if D==E:
            print("Yes")
        else:
            print("No")
    elif A==B:
        if C==D==E:
            print("Yes")
        else:
            print("No")
    elif A==C:
        if B==D==E:
            print("Yes")
        else:
            print("No")
    elif B==C:
        if A==D==E:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
main()
