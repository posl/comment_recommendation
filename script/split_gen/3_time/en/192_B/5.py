def main():
    s = input()
    print("Yes" if all([s[i].islower() if i % 2 == 0 else s[i].isupper() for i in range(len(s))]) else "No")
