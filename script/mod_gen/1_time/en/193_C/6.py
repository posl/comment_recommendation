def main():
    N = int(input())
    div = []
    for i in range(2, int(N ** 0.5) + 1):
        for j in range(2, 100):
            if i ** j <= N:
                div.append(i ** j)
            else:
                break
    print(N - len(set(div)))
main()

if __name__ == '__main__':
    main()