def main():
    N = int(input())
    count = 0
    for a in range(1, N+1):
        for b in range(a, N+1):
            if a*b > N:
                break
            for c in range(b, N+1):
                if a*b*c > N:
                    break
                if a == b and b == c:
                    count += 1
                elif a == b or b == c:
                    count += 3
                else:
                    count += 6
    print(count)

if __name__ == '__main__':
    main()