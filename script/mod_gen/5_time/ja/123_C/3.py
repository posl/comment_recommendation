def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    min_num = min(A,B,C,D,E)
    if N % min_num == 0:
        time = N // min_num
    else:
        time = N // min_num + 1
    print(time + 4)

if __name__ == '__main__':
    main()