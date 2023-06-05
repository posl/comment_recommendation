def split_pins(bowl):
    bowl = list(bowl)
    for i in range(10):
        bowl[i] = int(bowl[i])
    for i in range(10):
        if bowl[i] == 0:
            bowl[i] = 1
            break
    for i in range(10):
        if bowl[i] == 1:
            bowl[i] = 0
            break
    for i in range(10):
        if bowl[i] == 1:
            bowl[i] = 0
            break
    for i in range(10):
        if bowl[i] == 1:
            bowl[i] = 0
            break
    for i in range(10):
        if bowl[i] == 1:
            bowl[i] = 0
            break
    for i in range(10):
        if bowl[i] == 1:
            bowl[i] = 0
            break
    for i in range(10):
        if bowl[i] == 1:
            bowl[i] = 0
            break
    for i in range(10):
        if bowl[i] == 1:
            bowl[i] = 0
            break
    for i in range(10):
        if bowl[i] == 1:
            bowl[i] = 0
            break
    for i in range(10):
        if bowl[i] == 1:
            return "Yes"
    return "No"

if __name__ == '__main__':
    split_pins()