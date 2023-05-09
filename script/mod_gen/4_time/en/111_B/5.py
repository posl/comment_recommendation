def abc111_b():
    n = int(input())
    for i in range(1, 10):
        if n <= i * 111:
            print(i * 111)
            return

if __name__ == '__main__':
    abc111_b()