def main():
    # S,T = [input() for i in range(2)]
    S,T = input().split()
    print("Yes" if T in S else "No")

if __name__ == '__main__':
    main()