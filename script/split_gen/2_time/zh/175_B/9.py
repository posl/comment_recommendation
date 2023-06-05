def main():
    weather = input()
    count = 0
    max = 0
    for i in range(len(weather)):
        if weather[i] == 'R':
            count += 1
        else:
            count = 0
        if count > max:
            max = count
    print(max)
