def get_count(points):
    count = 0
    for i in range(0, len(points)):
        for j in range(i+1, len(points)):
            for k in range(j+1, len(points)):
                for l in range(k+1, len(points)):
                    if is_rectangle(points[i], points[j], points[k], points[l]):
                        count += 1
    return count

if __name__ == '__main__':
    get_count()