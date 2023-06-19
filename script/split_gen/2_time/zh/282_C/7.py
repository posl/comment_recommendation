def main():
    n = int(input())
    s = input()
    for i in range(0,n,2):
        s = s.replace(s[i],'.')
    print(s)
