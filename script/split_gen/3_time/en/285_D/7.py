def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s.append(input())
        t.append(input())
    for i in range(n):
        if s[i] in t:
            print('No')
            exit()
    print('Yes')
