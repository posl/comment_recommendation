def main():
    n = int(input())
    l = [int(x) for x in input().split()]
    l.sort(reverse=True)
    if l[0] < sum(l[1:]):
        print("Yes")
    else:
        print("No")
