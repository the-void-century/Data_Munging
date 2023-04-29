"""Dependency Injection Library"""
from injector import AssistedBuilder
from injector import Injector
from data_analysis import DataAnalyzer
from data_extraction import DataExtractor

injector = Injector()
update_extraction = injector.get(AssistedBuilder(cls=DataExtractor))
# inject2=Injector()
update_analyzer = injector.get(AssistedBuilder(cls=DataAnalyzer))


class Calculator():
    """This class calls the other classes"""

    def __init__(self, data_path):
        self.data = update_extraction.build(data_path=data_path)
        self.ans = update_analyzer.build(
            data=self.data.map_values_to_columns())

    def calculate(self, col1, col2, answer_col):
        """This function returns the required answer"""

        return self.ans.min_diff(col1, col2, answer_col)


def main():
    """This is the main function"""
    print("Please input the data path: ", end=" ")
    data_path = input()
    calc = Calculator(data_path)
    print("Please input the two columns you wish to calculate the minimum difference for:", end=" ")
    col1, col2 = map(str, input().split())
    print("Please input the what attribute of the answer you want to be displayed:", end=" ")
    answer_col = input()
    print(calc.calculate(col1, col2, answer_col))


if __name__ == "__main__":
    main()
