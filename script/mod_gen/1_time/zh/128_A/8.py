def max_pie(apple, piece):
    return min(apple * 3 + piece, (apple + piece) // 2)

if __name__ == '__main__':
    max_pie()