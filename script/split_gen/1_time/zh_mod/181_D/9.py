def main():
    s = input()
    s = sorted(s)
    if len(s) == 1:
        if int(s[0]) % 8 == 0:
