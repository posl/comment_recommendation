def main():
    n = int(input())
    a = [int(a) for a in input().split()]
    print(max(a)-min(a))
