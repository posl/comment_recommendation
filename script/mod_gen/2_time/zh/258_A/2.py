def main():
    K = int(input())
    hour = K // 60
    minute = K % 60
    print(f"{21 + hour:02}:{minute:02}")

if __name__ == '__main__':
    main()