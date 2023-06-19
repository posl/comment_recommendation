def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = set(a)
    print(len(b))
