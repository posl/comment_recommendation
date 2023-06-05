def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s.append(input())
        t.append(input())
    for i in range(n):
        for j in range(n):
            if i != j and s[i] == t[j]:
                print('No')
                return
    print('Yes')
