"""This module extracts and analyses data"""
from data_extraction import DataExtractor
from data_analysis import DataAnalyzer

class Calculator():
    """This class calls the other classes"""
    def __init__(self,extract,analyze,data_path):
        self.extract=extract
        self.analyze=analyze
        self.extract.set_data(data_path)
        self.analyze.set_data(extract.map_values_to_columns())
    def calculate(self, col1, col2, answer_col):
        """This function returns the required answer"""
        return self.analyze.min_diff(col1, col2, answer_col)


def main():
    """This is the main function"""
    extract=DataExtractor()
    analyze=DataAnalyzer()
    print("Please input the data path: ", end=" ")
    data_path = input()
    print("Please input the two columns you wish to calculate the minimum difference for:", end=" ")
    col1, col2 = map(str, input().split())
    print("Please input the what attribute of the answer you want to be displayed:", end=" ")
    answer_col = input()
    calculate=Calculator(extract,analyze,data_path)
    print(calculate.calculate(col1,col2,answer_col))


if __name__ == "__main__":
    main()
