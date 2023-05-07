def main():
    # Read input
    S = input()
    # Check if S is a substring of T
    T = "oxx" * 100000
    if S in T:
        print("Yes")
    else:
        print("No")
