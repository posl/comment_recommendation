def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    print(max(0, min(B) - max(A) + 1))
main()
