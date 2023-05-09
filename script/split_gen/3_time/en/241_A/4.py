def main():
    a = input().split()
    b = []
    for i in a:
        b.append(int(i))
    count = 0
    while True:
        if count == 3:
            print(b[0])
            break
        else:
            count += 1
            b[0] = b[b[0]]
