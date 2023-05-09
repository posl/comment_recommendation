def main():
    S, T, X = map(int, input().split())
    if (X >= S and X < T) or (S > T and (X >= S or X < T)):
        print("Yes")
    else:
        print("No")
