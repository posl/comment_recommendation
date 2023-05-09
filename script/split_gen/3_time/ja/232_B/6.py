def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    for k in range(1, 26):
        if s == t[k:] + t[:k]:
            print("Yes")
            return
    print("No")
