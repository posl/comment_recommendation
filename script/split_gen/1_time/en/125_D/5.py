def main():
    n = int(input())
    a = list(map(int, input().split()))
    if n%2==0:
        print(sum([abs(i) for i in a]))
    else:
        print(sum([abs(i) for i in a[1:]]) - a[0])
