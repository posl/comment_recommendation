def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    if a[-1] < sum(a[:-1]):
        print("Yes")
    else:
        print("No")
