def main():
    n = int(input())
    print("Yay!") if int(n*1.08) < 206 else print(":(") if int(n*1.08) > 206 else print("so-so")

if __name__ == '__main__':
    main()