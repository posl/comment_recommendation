def main():
    s = input()
    t = input()
    for i in range(len(s)+1):
        if s[:i] + s[i-1:] == t:
            print(i)
            break
