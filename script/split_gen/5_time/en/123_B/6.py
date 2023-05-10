def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    time = 0
    time += a
    if time % 10 != 0:
        time += 10 - time % 10
    time += b
    if time % 10 != 0:
        time += 10 - time % 10
    time += c
    if time % 10 != 0:
        time += 10 - time % 10
    time += d
    if time % 10 != 0:
        time += 10 - time % 10
    time += e
    print(time)
