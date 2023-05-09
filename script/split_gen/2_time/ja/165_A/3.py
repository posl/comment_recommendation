def main():
    k = int(input())
    a, b = map(int, input().split())
    if a % k == 0:
        print("OK")
        return
    if b % k == 0:
        print("OK")
        return
    if a // k == b // k:
        print("NG")
        return
    print("OK")
