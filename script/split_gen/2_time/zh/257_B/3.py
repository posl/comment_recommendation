def main():
    n, x = map(int, input().split())
    print(chr((x-1)%26 + 65))
