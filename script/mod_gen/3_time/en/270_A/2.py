def main():
    a, b = map(int, input().split())
    sol = 0
    if a == 1:
        sol += 300000
    elif a == 2:
        sol += 200000
    elif a == 3:
        sol += 100000
    if b == 1:
        sol += 300000
    elif b == 2:
        sol += 200000
    elif b == 3:
        sol += 100000
    if a == b == 1:
        sol += 400000
    print(sol)
main()

if __name__ == '__main__':
    main()