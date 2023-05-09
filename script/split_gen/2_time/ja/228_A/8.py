def main():
    S, T, X = map(int, input().split())
    if S <= X and X < T:
        print("Yes")
    elif S == T:
        print("No")
    else:
        if S > T:
            if X >= S or X < T:
                print("Yes")
            else:
                print("No")
        else:
            print("No")
