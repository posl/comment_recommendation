def main():
    k = int(input())
    a, b = map(int, input().split())
    a = int(str(a), k)
    b = int(str(b), k)
    print(a * b)
