def main():
    A, B, C = map(int, input().split())
    print(100*(A*(B+C)+B*C)/(A+B+C)**2)

if __name__ == '__main__':
    main()