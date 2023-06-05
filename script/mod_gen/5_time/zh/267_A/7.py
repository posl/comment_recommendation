def main():
    week = ['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
    s = input()
    for i in range(7):
        if s == week[i]:
            break
    print(7-i)

if __name__ == '__main__':
    main()