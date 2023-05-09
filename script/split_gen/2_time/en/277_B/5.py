def main():
    n = int(input())
    s = set()
    for i in range(n):
        s.add(input())
    print('Yes' if len(s) == n and all(s[i][1] in 'A23456789TJQK' for i in range(n)) and all(s[i][0] in 'HDCS' for i in range(n)) else 'No')
