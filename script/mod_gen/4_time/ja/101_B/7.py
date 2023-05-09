def check(n):
    #print(n)
    #print(sum(list(map(int, str(n)))))
    #print(n % sum(list(map(int, str(n)))))
    if n % sum(list(map(int, str(n)))) == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    check()