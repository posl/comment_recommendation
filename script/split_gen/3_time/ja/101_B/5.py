def main():
    n = input()
    s = 0
    for c in n:
        s += int(c)
    print("Yes" if int(n) % s == 0 else "No")
