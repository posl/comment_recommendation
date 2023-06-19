def main():
    s = input()
    t = input()
    if len(s) == len(t):
        for i in range(len(s)):
            if s == t:
                print('Yes')
                break
            s = s[-1] + s[0:-1]
        else:
            print('No')
    else:
        print('No')
