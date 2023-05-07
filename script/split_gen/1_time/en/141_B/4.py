def main():
    s = input()
    for i, c in enumerate(s):
        if i % 2 == 0 and c in ['L']:
            print('No')
            return
        elif i % 2 == 1 and c in ['R']:
            print('No')
            return
    print('Yes')
    return
