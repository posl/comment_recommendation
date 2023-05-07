def pascal_triangle(row):
    if row==0:
        return [1]
    elif row==1:
        return [1,1]
    else:
        prev_row=pascal_triangle(row-1)
        new_row=[1]
        for i in range(len(prev_row)-1):
            new_row.append(prev_row[i]+prev_row[i+1])
        new_row.append(1)
        return new_row
