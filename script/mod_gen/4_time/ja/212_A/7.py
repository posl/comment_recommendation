def problems212_a():
    a, b = map(int, input().split())
    if 0 < a and b == 0:
        print("Gold")
    elif a == 0 and 0 < b:
        print("Silver")
    else:
        print("Alloy")

if __name__ == '__main__':
    problems212_a()