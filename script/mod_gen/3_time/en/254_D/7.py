def main():
    N = int(input())
    answer = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i * j == int(i * j ** 0.5) ** 2:
                answer += 1
    print(answer)

if __name__ == '__main__':
    main()