def main():
    N = int(input())
    tax_included = int(N * 1.08)
    if tax_included < 206:
        print("Yay!")
    elif tax_included == 206:
        print("so-so")
    else:
        print(":(")
main()
You can also use the floor division operator (//) to get the same result as int().

if __name__ == '__main__':
    main()