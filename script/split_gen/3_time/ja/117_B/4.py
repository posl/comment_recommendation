def main():
    N = int(input())
    L = [int(x) for x in input().split()]
    L.sort(reverse=True)
    if L[0] < sum(L[1:]):
        print("Yes")
    else:
        print("No")
