def main():
    k = int(input())
    h = 21 + k // 60
    m = k % 60
    print(f"{h:02}:{m:02}")

if __name__ == '__main__':
    main()