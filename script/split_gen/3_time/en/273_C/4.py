def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = list(set(a))
    a.sort()
    print(a)
