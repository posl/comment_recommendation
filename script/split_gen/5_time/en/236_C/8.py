def main():
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()
    if len(s) == len(t):
        print("Yes")
    else:
        print("No")
