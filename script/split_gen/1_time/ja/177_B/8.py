def main():
    s = input()
    t = input()
    print(len(t) - max([len([1 for i in range(len(t)) if s[i+j] == t[i]]) for j in range(len(s)-len(t)+1)]))
