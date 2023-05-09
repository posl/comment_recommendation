def main():
    n,x = map(int,input().split())
    s = input()
    for i in range(n):
        if s[i] == "U":
            x = (x-2)//2 + 1
        elif s[i] == "L":
            x = x*2 - 1
        else:
            x = x*2
    print(x)
