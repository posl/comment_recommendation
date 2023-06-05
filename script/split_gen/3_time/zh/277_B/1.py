def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    for i in range(n-1):
        if s[i] == s[i+1]:
            print('No')
            exit()
    print('Yes')
