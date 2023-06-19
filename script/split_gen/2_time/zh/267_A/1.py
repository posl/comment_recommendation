def main():
    day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    s = input()
    for i in range(len(day)):
        if s == day[i]:
            print(5 - i)
            break
