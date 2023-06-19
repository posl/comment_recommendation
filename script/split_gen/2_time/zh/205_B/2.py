def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a == list(range(1, n+1)):
        print("Yes")
    else:
        print("No")
