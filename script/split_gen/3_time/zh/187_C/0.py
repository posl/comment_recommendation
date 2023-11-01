def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    for i in range(n):
        if s[i][0] == '!': 
            if s[i][1:] in s:
