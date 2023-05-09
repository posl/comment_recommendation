def main():
    n = int(input())
    a = list(map(int, input().split()))
    if len(set(a)) == len(a):
        print("YES")
    else:
        print("NO")
