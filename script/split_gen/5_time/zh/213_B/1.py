def main():
    n = int(input())
    a = list(map(int,input().split()))
    second = min(a)
    a.remove(second)
    print(a.index(min(a))+2)
