def main():
    s = input()
    t = input()
    for i in range(len(t)):
        if t[:i] + t[i+1:] == s:
            print(i+1)
            break
