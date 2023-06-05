def main():
    N = input()
    sum = 0
    for i in N:
        sum += int(i)
    if sum % 9 == 0:
        print('Yes')
    else:
        print('No')
