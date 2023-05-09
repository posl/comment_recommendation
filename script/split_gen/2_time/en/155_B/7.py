def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    for i in A:
        if i % 2 == 0 and i % 3 != 0 and i % 5 != 0:
            print("DENIED")
            return
    print("APPROVED")
