def main():
    K = int(input())
    print(f"{21 + (K // 60):02}:{(K % 60):02}")

if __name__ == '__main__':
    main()