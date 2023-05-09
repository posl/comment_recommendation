def main():
    k = int(input())
    a, b = map(int, input().split())
    a10 = int(str(a), k)
    b10 = int(str(b), k)
    print(a10 * b10)
