def get_input():
    A,B = map(int,input().split())
    if 1 <= A <= B <= 20:
        return A,B
    else:
        print("输入不符合要求，请重新输入")
        return get_input()

if __name__ == '__main__':
    get_input()