import os

def rename(path):
    files = os.listdir(path)
    files = sorted(files)
    for file in files:
        os.rename(path + file, path + file.upper())

if __name__ == '__main__':
    path = '/Users/keikoyanagi/Desktop/comment_recommendation/test_case/'
    rename(path)