def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    result = 1
    for i in range(n):
        if s[i] == "OR":
            result += 2**(i+1)
    print(result)

if __name__ == '__main__':
    main()