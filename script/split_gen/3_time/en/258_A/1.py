def main():
    k = int(input())
    hour = 21 + k // 60
    minute = k % 60
    if hour >= 24:
        hour -= 24
    print('{:02}:{:02}'.format(hour, minute))
