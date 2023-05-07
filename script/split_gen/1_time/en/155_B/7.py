def main():
    N = int(input())
    A = list(map(int, input().split()))
    for a in A:
        if a % 2 == 0 and not a % 3 == 0 and not a % 5 == 0:
            print("DENIED")
            return
    print("APPROVED")
