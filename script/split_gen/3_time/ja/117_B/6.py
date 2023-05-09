def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    if l[n-1] < sum(l[:n-1]):
        print("Yes")
    else:
        print("No")
