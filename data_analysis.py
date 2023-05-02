"""Analyzes the given file based on given attributes"""
class DataAnalyzer():
    """This class analyses the given data"""
    def __init__(self):
        self.data={}
        #print(self.data)
    def set_data(self,data):
        self.data=data
    def min_diff(self,col1,col2,answer_col):
        """This function finds the minimum 
        difference between two values in a column and returns
        its corresponding first value"""
        minimum_difference=1e7
        answer_value=""
        for i in range(len(self.data[col1])):
            try:
                curr_diff=abs(float(self.data[col1][i])
                                          -float(self.data[col2][i]))
                if minimum_difference>curr_diff:
                    minimum_difference=curr_diff
                    answer_value=self.data[answer_col][i]
            except ValueError:
                pass
        return answer_value
