def main():
    string = input()
    ball = []
    for i in range(len(string)):
        if string[i] == '(':
            pass
        elif string[i] == ')':
            if len(ball) > 0:
                ball.pop()
            else:
                print('No')
                return
        else:
            ball.append(string[i])
    print('Yes')
    return

if __name__ == '__main__':
    main()