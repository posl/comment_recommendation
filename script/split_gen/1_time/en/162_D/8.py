def main():
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    print(r*g*b - sum(s[i] == s[j] == s[k] for i in range(n) for j in range(i+1, n) for k in range(j+1, n) if j-i != k-j))
