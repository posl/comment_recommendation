def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s = [x[1:] if x[0]=='!' else x for x in s]
    s.sort()
    for i in range(n-1):
        if s[i] == s[i+1]:
            print(s[i])
            return
    print('satisfiable')
