def main():
    a, b, c, k = map(int, input().split())
    answer = 0
    if a >= k:
        answer = k
    elif a + b >= k:
        answer = a
    else:
        answer = a - (k - a - b)
    print(answer)

if __name__ == '__main__':
    main()