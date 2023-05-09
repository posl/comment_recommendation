def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(1, 26):
        if "".join([chr((ord(c) - ord("a") + i) % 26 + ord("a")) for c in S]) == T:
            print("Yes")
            return
    print("No")
