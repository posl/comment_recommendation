def solve():
    S = input()
    T = input()
    for i in range(len(T)+1):
        if S[:i].replace("?", "a") + S[-len(T)+i:].replace("?", "a") == T:
            print("Yes")
        else:
            print("No")
solve()

if __name__ == '__main__':
    solve()