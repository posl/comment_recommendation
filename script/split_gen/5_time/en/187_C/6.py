def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s = sorted(s)
    for i in range(n-1):
        if s[i][0] == "!" and s[i+1] == s[i][1:]:
            print(s[i+1])
            return
    print("satisfiable")
