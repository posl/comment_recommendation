def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    a = set(a)
    a = sorted(a)
    a = list(reversed(a))
    a = set(a)
    a = sorted(a)
    a = list(reversed(a))
    print(len(a))