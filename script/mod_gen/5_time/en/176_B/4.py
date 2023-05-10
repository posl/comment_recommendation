def check_multiple_of_9(n):
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    if sum % 9 == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    check_multiple_of_9()