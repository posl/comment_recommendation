def main():
    S = input()
    T = "o" + "x" * 10**5
    if S in T:
        print("Yes")
    else:
        print("No")
