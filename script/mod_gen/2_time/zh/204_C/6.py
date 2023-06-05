def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    answer = 0
    for a in A:
        if a > 10:
            answer += a - 10
    print(answer)

if __name__ == '__main__':
    main()