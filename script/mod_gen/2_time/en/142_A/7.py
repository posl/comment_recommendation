def main():
    n = int(input())
    print('{:.10f}'.format(0.5 if n % 2 == 0 else 1))

if __name__ == '__main__':
    main()