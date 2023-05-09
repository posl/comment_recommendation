def main():
    number = int(input())
    counter = 0
    for i in range(1, number + 1):
        if len(str(i)) % 2 != 0:
            counter += 1
    print(counter)
