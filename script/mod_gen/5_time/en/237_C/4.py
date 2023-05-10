def solve():
    S = input()
    #print(S)
    #print(S[::-1])
    if S == S[::-1]:
        print("Yes")
    else:
        print("No")
    return 0

if __name__ == '__main__':
    solve()