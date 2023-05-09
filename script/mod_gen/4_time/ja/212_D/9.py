def main():
    n = int(input())
    #print(n)
    ball = []
    for i in range(n):
        #print(i)
        a = input()
        #print(a)
        if a[0] == '1':
            b = a.split()
            #print(b)
            ball.append(int(b[1]))
            #print(ball)
        elif a[0] == '2':
            b = a.split()
            #print(b)
            for j in range(len(ball)):
                ball[j] += int(b[1])
            #print(ball)
        else:
            print(min(ball))
            ball.remove(min(ball))
            #print(ball)

if __name__ == '__main__':
    main()