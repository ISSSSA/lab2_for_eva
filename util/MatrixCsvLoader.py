import csv
import os

from domain.InputData import InputData


class MatrixCsvLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        result = []
        with open(os.getcwd() + self.file_path, mode='r', newline='') as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)  # Пропускаем заголовок
            for row in reader:
                data = list(map(float, row[:len(row)-2]))  # Все, кроме последнего элемента
                label = row[-2]  # Последний элемент (метка)
                result.append(InputData(data, label))
        return result
