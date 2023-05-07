def main():
    k = int(input())
    a, b = map(int, input().split())
    if a % k == 0 or b % k == 0:
        print("OK")
    elif a // k + 1 <= b // k:
        print("OK")
    else:
        print("NG")
