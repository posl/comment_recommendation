def main():
    S = input()
    S = S[::-1]
    S = "a" + S
    if S == S[::-1]:
        print("Yes")
    else:
        print("No")
