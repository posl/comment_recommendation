def main():
    n = int(input())
    a = input().split()
    b = [int(i) for i in a]
    b.sort()
    if b == list(range(1, n+1)):
        print("Yes")
    else:
        print("No")
