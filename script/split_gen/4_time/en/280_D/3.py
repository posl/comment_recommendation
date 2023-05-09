def main():
    k = int(input())
    i = 1
    while True:
        if i % k == 0:
            print(i)
            break
        else:
            i += 1
