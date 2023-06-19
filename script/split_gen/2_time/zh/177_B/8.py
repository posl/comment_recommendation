def main():
    s = input()
    t = input()
    print(len(t) - max([s[i:].find(t) for i in range(len(s))]))
