def main():
    n = int(input())
    s = 0
    for c in str(n):
        s += int(c)
    if n % s == 0:
        print('Yes')
    else:
        print('No')
