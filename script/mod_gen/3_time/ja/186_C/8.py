def main():
    n = int(input())
    result = 0
    for i in range(1, n+1):
        if '7' in str(i) or '7' in str(oct(i)):
            continue
        else:
            result += 1
    print(result)

if __name__ == '__main__':
    main()