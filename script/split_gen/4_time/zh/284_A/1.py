def main():
    n = int(input())
    s = [input() for i in range(n)]
    for i in range(n-1,-1,-1):
        print(s[i])
