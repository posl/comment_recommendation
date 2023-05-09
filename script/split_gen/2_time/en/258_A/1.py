def main():
    k = int(input())
    hour = k // 60
    minute = k % 60
    print(str(21 + hour).zfill(2) + ":" + str(minute).zfill(2))
