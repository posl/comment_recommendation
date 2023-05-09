def main():
    S, T, X = map(int, input().split())
    if S <= X and X < T:
        print("Yes")
    elif S == 23 and T == 0 and X == 23:
        print("Yes")
    else:
        print("No")
