def main():
    a = input().split()
    sum = 0
    for i in range(len(a)):
        sum += int(a[i])
    if sum >= 22:
