def main():
    k = int(input())
    print(f"{21 + k // 60:02}:{k % 60:02}")

if __name__ == '__main__':
    main()