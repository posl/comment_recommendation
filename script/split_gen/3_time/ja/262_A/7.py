def main():
    y = int(input())
    for i in range(4):
        if (y+i)%4 == 2:
            print(y+i)
            break
