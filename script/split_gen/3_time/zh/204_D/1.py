def main():
    n = int(input())
    t = list(map(int,input().split()))
    t.sort()
    print(t[-1]+t[-2])
