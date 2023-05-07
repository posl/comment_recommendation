def main():
    #write your code here
    k = int(input())
    hour = 21 + k // 60
    minute = k % 60
    print(str(hour) + ":" + str(minute))

if __name__ == '__main__':
    main()