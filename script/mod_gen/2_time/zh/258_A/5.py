def main():
    k = int(input())
    hour = k // 60
    minute = k % 60
    if hour < 10:
        hour = '0'+str(hour)
    if minute < 10:
        minute = '0'+str(minute)
    print(str(21+hour)+':'+str(minute))

if __name__ == '__main__':
    main()