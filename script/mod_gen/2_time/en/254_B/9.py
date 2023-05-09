def main():
    N = int(input())
    # N = 10
    for i in range(N):
        if i == 0:
            print(1)
        else:
            a = [1]
            for j in range(1, i+1):
                a.append(a[j-1] * (i+1-j) // j)
            print(" ".join(map(str, a)))

if __name__ == '__main__':
    main()