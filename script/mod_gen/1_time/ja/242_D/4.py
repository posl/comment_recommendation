def main():
    s = input()
    q = int(input())
    s_list = list(s)
    a = s_list.count("A")
    b = s_list.count("B")
    c = s_list.count("C")
    for i in range(q):
        ti, ki = map(int, input().split())
        if ti % 3 == 1:
            if ki <= a:
                print("A")
            elif ki <= a + b:
                print("B")
            else:
                print("C")
        elif ti % 3 == 2:
            if ki <= b:
                print("B")
            elif ki <= a + b:
                print("C")
            else:
                print("A")
        else:
            if ki <= c:
                print("C")
            elif ki <= a + c:
                print("A")
            else:
                print("B")

if __name__ == '__main__':
    main()