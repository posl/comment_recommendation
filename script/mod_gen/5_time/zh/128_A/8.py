def make_pie(apple, piece):
    if apple == 0:
        return 0
    else:
        return int(apple / 2) * 3 + (apple % 2) + int(piece / 2) * 3 + (piece % 2)
    
apple, piece = input().split()
apple = int(apple)
piece = int(piece)
print(make_pie(apple, piece))
