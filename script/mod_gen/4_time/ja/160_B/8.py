def exchange(x):
    # 500円玉
    fivehundred = x // 500
    # 100円玉
    onehundred = (x - fivehundred * 500) // 100
    # 50円玉
    fifty = (x - fivehundred * 500 - onehundred * 100) // 50
    # 10円玉
    ten = (x - fivehundred * 500 - onehundred * 100 - fifty * 50) // 10
    # 5円玉
    five = (x - fivehundred * 500 - onehundred * 100 - fifty * 50 - ten * 10) // 5
    # 1円玉
    one = x - fivehundred * 500 - onehundred * 100 - fifty * 50 - ten * 10 - five * 5
    return fivehundred * 1000 + onehundred * 100 + fifty * 10 + five * 2
x = int(input())
print(exchange(x))

if __name__ == '__main__':
    exchange()