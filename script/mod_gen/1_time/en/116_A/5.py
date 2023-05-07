def main():
    #Read the input
    ab, bc, ca = map(int, input().split())
    #Calculate the area
    area = int((ab * bc) / 2)
    #Print the area
    print(area)

if __name__ == '__main__':
    main()