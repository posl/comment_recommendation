def main():
    K = int(input())
    if K < 60:
        print("21:{}".format(60 + K))
    else:
        hour = 21 + (K // 60)
        minute = 60 + (K % 60)
        if minute >= 60:
            hour += 1
            minute -= 60
        print("{}:{}".format(hour, minute))
