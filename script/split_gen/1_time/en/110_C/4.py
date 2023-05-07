def main():
    S = list(input())
    T = list(input())
    S = sorted(S)
    T = sorted(T, reverse = True)
    if S < T:
        print("Yes")
    else:
        print("No")
