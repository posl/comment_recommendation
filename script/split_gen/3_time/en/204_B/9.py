def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N != len(A):
        print("Error: N != len(A)")
        return
    if N < 1 or N > 1000:
        print("Error: N is out of range")
        return
    for a in A:
        if a < 0 or a > 1000:
            print("Error: A is out of range")
            return
    ans = 0
    for a in A:
        if a > 10:
            ans += a - 10
    print(ans)
main()
