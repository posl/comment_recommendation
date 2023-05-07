def main():
    #input the values of the sides
    a, b, c = map(int, input().split())
    #calculate the area of the triangle
    area = int(a * b * 0.5)
    #print the area of the triangle
    print(area)
main()

if __name__ == '__main__':
    main()