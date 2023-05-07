def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    for i in range(1, 26):
        if "".join([chr((ord(c) - ord("a") + i) % 26 + ord("a")) for c in s]) == t:
            print("Yes")
            return
    print("No")
