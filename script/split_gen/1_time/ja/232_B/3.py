def main():
    S = input()
    T = input()
    for i in range(26):
        if S == T:
            print("Yes")
            return
        S = "".join([chr((ord(s) - ord("a") + 1) % 26 + ord("a")) for s in S])
    print("No")
