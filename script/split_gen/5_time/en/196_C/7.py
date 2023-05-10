def main():
    N = int(input())
    s = str(N)
    l = len(s)
    if l == 1:
        print(0)
    else:
        if l % 2 == 0:
            print(int(s[:l//2]) - 1)
        else:
            print(int(s[:l//2]))
