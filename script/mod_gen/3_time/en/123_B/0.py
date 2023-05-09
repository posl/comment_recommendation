def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    min_time = min(A%10, B%10, C%10, D%10, E%10)
    if min_time == 0:
        print(A+B+C+D+E)
    else:
        print(A+B+C+D+E-10+min_time)

if __name__ == '__main__':
    main()