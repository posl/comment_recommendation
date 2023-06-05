def get_num_of_triangles(lengths):
    lengths.sort()
    num_of_triangles = 0
    for i in range(len(lengths)):
        for j in range(i + 1, len(lengths)):
            for k in range(j + 1, len(lengths)):
                if lengths[i] + lengths[j] > lengths[k]:
                    num_of_triangles += 1
    return num_of_triangles
