def main():
    day = input()
    week = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    count = 0
    for i in range(7):
        if day == week[i]:
            count = i
            break
    if count < 5:
        print(5-count)
    else:
        print(7-count+5)
