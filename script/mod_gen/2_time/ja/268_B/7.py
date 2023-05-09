def solve():
    S = input()
    T = input()
    if T[:len(S)] == S:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()