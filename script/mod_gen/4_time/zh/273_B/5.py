def main():
    x,k = map(int,input().split())
    result = x
    for i in range(k):
        result = (result//10)*10
        if x%10 >= 5:
            result += 10
        x = result
    print(result)

if __name__ == '__main__':
    main()