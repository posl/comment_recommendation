def main():
    # read the input
    D, T, S = map(int, input().split())
    # determine if he will arrive in time
    if D/S <= T:
        print("Yes")
    else:
        print("No")
