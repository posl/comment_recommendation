def main():
    p = list(map(int, input().split()))
    s = [chr(ord('a') + i - 1) for i in p]
    print("".join(s))
