def main():
    for i in range(10):
        s = input()
        if '#' in s:
            left = i + 1
            break
    for i in range(9, -1, -1):
        s = input()
        if '#' in s:
            right = i + 1
            break
    for i in range(10):
        s = input()
        if '#' in s:
            top = i + 1
            break
    for i in range(9, -1, -1):
        s = input()
        if '#' in s:
            bottom = i + 1
            break
    print(left, top)
    print(right, bottom)
