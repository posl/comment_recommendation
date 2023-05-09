def main():
    n = int(input())
    if n >= 42:
        print(f"AGC{n+1}")
    else:
        print(f"AGC{n:03}")

if __name__ == '__main__':
    main()