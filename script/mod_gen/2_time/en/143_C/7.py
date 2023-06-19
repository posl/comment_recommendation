def main():
    n = int(input())
    s = input()
    result = 1
    for i in range(1, n):
        if s[i] != s[i-1]:
            result += 1
    print(result)
main()
