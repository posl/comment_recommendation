def main():
    S = input()
    S = S[::-1]
    S = S + "a"
    S = S[::-1]
    if S == S[::-1]:
        print("Yes")
    else:
        print("No")
