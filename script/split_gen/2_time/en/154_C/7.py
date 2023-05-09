def main():
    n = int(input())
    a = list(map(int, input().split()))
    if n == len(set(a)):
        print("YES")
    else:
        print("NO")
