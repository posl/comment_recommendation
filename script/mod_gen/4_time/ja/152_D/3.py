def main():
    N = int(input())
    count = 0
    for i in range(1,N+1):
        i = str(i)
        if i[0] == i[-1]:
            count += 1
    print(count)
main()
