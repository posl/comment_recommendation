def main():
    a,b = input().split()
    a_sum = 0
    b_sum = 0
    for i in range(len(a)):
        a_sum += int(a[i])
        b_sum += int(b[i])
    if a_sum > b_sum:
        print(a_sum)
    else:
        print(b_sum)
