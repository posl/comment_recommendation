def main():
    n, x = map(int, input().split())
    s = input()
    for i in range(n):
        if s[i] == "L":
            x = x*2 - 1
        elif s[i] == "R":
            x = x*2 + 1
        else:
            if x % 2 == 0:
                x = (x-1)//2
            else:
                x = x//2
    print(x)
