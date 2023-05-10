def main():
    n = int(input())
    a = list(map(int, input().split()))
    a2 = sorted(a)
    print(a.index(a2[1])+1)
