def main():
    V, T, S, D = map(int, input().split())
    print("Yes" if D < V * T or D > V * S else "No")
    return

if __name__ == '__main__':
    main()