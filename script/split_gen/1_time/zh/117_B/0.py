def main():
    n = int(input())
    ls = list(map(int, input().split()))
    ls.sort()
    if ls[-1] < sum(ls[:-1]):
