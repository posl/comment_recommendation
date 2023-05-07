def main():
    #Read the data from the input file
    f = open('input.txt', 'r')
    data = f.read()
    f.close()
    #Split the data into lines, and then into rows
    lines = data.split('
')
    rows = [line.split(' ') for line in lines]
    #Convert the rows into integers, and then into a 2x2 array
    matrix = [[int(row) for row in row] for row in rows]
    #Print the matrix
    print(matrix)
