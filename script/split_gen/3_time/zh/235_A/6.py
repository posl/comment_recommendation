def main():
    abc = int(input())
    bca = int(str(abc)[1:] + str(abc)[0])
    cab = int(str(abc)[2:] + str(abc)[:2])
    print(abc + bca + cab)
