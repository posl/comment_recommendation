def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    print(max(a) - min(a))
