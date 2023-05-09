def main():
    x = input()
    if x.find('.') == -1:
        print(x)
    else:
        print(x[:x.find('.')])
    return
