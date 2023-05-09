def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(1, 26):
        S = "".join([chr((ord(c) - ord("a") + i) % 26 + ord("a")) for c in S])
        if S == T:
            print("Yes")
            return
    print("No")
