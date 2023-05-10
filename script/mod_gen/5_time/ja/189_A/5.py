def main():
    C_1, C_2, C_3 = input().split()
    if C_1 == C_2 and C_2 == C_3:
        print("Won")
    else:
        print("Lost")

if __name__ == '__main__':
    main()