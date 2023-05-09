def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    min_people = min(A,B,C,D,E)
    min_time = N // min_people
    if N % min_people != 0:
        min_time += 1
    min_time += 4
    print(min_time)

if __name__ == '__main__':
    main()