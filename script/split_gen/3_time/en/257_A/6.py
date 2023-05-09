def main():
    n,x = map(int,input().split())
    s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(n):
        print(s[x%26-1],end='')
        x = (x-1)//26
    print()
