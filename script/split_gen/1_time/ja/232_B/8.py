def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    for i in range(1, 26):
        if t == "".join([chr(((ord(c) - 97 + i) % 26) + 97) for c in s]):
            print("Yes")
            return
    print("No")
