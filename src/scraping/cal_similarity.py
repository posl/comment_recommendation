import Levenshtein
import sys
import os

class CalSimilarity():
    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2
        self.similarity = 0

    def cal_similarity(self):
        with open(self.file1, 'r') as f1:
            with open(self.file2, 'r') as f2:
                self.similarity = Levenshtein.ratio(f1.read(), f2.read())
        return self.similarity

    def get_similarity(self):
        return self.similarity