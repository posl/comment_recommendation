def main():
    k = int(input())
    i = 1
    while k > 0:
        if i % sum(map(int, str(i))) == 0:
            print(i)
            k -= 1
        i += 1
main()
