def main():
    N = int(input())
    count = 0
    for i in range(1,N+1):
        if "7" in str(i) or "5" in str(i) or "3" in str(i):
            count += 1
    print(count)
main()
