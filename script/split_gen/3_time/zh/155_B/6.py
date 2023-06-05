def main():
    n = int(input())
    a = list(map(int, input().split()))
    print("APPROVED" if all(x % 2 == 1 or x % 3 == 0 or x % 5 == 0 for x in a) else "DENIED")
