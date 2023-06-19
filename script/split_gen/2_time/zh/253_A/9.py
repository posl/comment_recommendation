def main():
    a,b,c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    if (b >= a and b <= c) or (b <= a and b >= c):
        print("Yes")
    else:
        print("No")
