def main():
    N = input()
    N = N[::-1]
    N = N.lstrip("0")
    N2 = N[::-1]
    if N == N2:
        print("Yes")
    else:
        print("No")
