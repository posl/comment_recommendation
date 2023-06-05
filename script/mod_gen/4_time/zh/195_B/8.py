def count_orange(a,b,w):
    min = 0
    max = 0
    if w%a == 0:
        min = w//a
    else:
        min = w//a + 1
    if w%b == 0:
        max = w//b
    else:
        max = w//b
    if max < min:
        print("UNSATISFIABLE")
    else:
        print(min,max)

if __name__ == '__main__':
    count_orange()