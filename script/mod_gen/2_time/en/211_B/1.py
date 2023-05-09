def main():
    S = [input() for _ in range(4)]
    if "H" in S and "2B" in S and "3B" in S and "HR" in S:
        print("Yes")
    else:
        print("No")
main()

if __name__ == '__main__':
    main()