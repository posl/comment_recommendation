def main():
    V, A, B, C = map(int, input().split())
    if V >= A+B+C:
        print('T')
    elif V >= A+B:
        print('M')
    elif V >= A:
        print('F')
    else:
        print('T')

if __name__ == '__main__':
    main()