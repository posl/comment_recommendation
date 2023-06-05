def main():
    K = int(input())
    if K < 2 or K > 100:
        print("K must between 2 and 100")
        return
    result = 0
    for i in range(1, K+1):
        for j in range(1, K+1):
            if i % 2 == 0 and j % 2 == 1:
                result += 1
    print(result)

if __name__ == '__main__':
    main()