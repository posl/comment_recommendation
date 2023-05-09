def main():
    A, B = map(int, input().split())
    answer = 100 - (B / A) * 100
    print(answer)

if __name__ == '__main__':
    main()