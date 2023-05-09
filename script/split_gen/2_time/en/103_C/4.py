def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = sum(a) - n
    print(ans)
