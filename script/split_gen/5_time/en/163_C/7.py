def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a
    for i in range(1, n+1):
        print(a.count(i))
