def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    ans = 0
    ans += (N + A - 1) // A
    ans += (N + B - 1) // B
    ans += (N + C - 1) // C
    ans += (N + D - 1) // D
    ans += (N + E - 1) // E
    ans += 4
    print(ans)
main()
