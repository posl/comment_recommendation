def main():
    k = int(input())
    a, b = map(int, input().split())
    if a % k == 0 or b % k == 0 or (a // k) < (b // k):
        print("OK")
    else:
        print("NG")
main()
