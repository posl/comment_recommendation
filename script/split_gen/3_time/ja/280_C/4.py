def main():
    s = input()
    t = input()
    for i in range(len(t)):
        if s[i] != t[i]:
            print(i)
            break
