def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if len(str(i)) % 2 == 0:
            if str(i)[0:int(len(str(i))/2)] == str(i)[int(len(str(i))/2):len(str(i))]:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()