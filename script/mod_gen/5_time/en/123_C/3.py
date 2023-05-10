def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    min_people = min(A,B,C,D,E)
    if N % min_people == 0:
        print(int(N/min_people) + 4)
    else:
        print(int(N/min_people) + 5)

if __name__ == '__main__':
    main()