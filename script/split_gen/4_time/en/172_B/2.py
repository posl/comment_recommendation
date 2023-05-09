def main():
    s = input()
    t = input()
    counter = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            counter += 1
    print(counter)
