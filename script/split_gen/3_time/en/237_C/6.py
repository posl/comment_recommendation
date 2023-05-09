def main():
    S = input()
    s = S
    S = S[::-1]
    if S == s:
        print("Yes")
    else:
        print("No")
