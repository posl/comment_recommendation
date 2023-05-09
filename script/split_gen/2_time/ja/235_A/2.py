def main():
    abc = input()
    x = abc[0]
    y = abc[1]
    z = abc[2]
    xyz = int(x+y+z)
    bca = int(y+z+x)
    cab = int(z+x+y)
    print(xyz+bca+cab)
