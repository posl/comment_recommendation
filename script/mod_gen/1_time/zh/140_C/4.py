def main():
    n = int(input())
    b = list(map(int, input().split()))
    a = []
    a.append(b[0])
    for i in range(n-2):
        a.append(min(b[i], b[i+1]))
    a.append(b[-1])
    print(sum(a))

if __name__ == '__main__':
    main()