def main():
    x = input()
    if x.find('.') != -1:
        print(x[0:x.find('.')])
    else:
        print(x)
