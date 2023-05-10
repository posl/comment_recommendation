def main():
    K = int(input())
    hour = K // 60
    minute = K % 60
    if hour > 23:
        hour = hour % 24
    print('{0:02d}:{1:02d}'.format(hour, minute))

if __name__ == '__main__':
    main()