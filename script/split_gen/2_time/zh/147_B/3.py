def main():
    a = input()
    a = a.split()
    sum = 0
    for i in range(3):
        sum += int(a[i])
    if sum >= 22:
        print('bust')
    else:
        print('win')
