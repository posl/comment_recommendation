def solve():
    S = input()
    if S.find("oo") != -1:
        print("Yes")
    elif S.find("xx") != -1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()