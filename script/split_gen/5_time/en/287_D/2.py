def main():
    s = input()
    t = input()
    for i in range(len(t)+1):
        if s[:i] + t[i:] == s[:i] + t[i:]:
            print('Yes')
        else:
            print('No')
