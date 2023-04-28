class DataExtractor():
    """This class is solely reponsible for data extraction from text files provided"""

    def __init__(self, data_path):
        self.data = []
        self.column_names = {}
        self.transformed_data = {}
        self.is_column_area={}
        with open(data_path, 'r', encoding='utf-8') as text_file:
            for rows in list(text_file):
                self.data.append(rows)

    def _get_column_indexes(self):
        """This function maps column indexes to their respective names"""
        curr_column_name = ""
        prev_index = 0
        for curr_index in range(len(self.data[0])):
            exception=[' ','\n']
            if self.data[0][curr_index] not in exception:
                # print(self.data[0][curr_index])
                if curr_column_name == "":
                    prev_index = curr_index
                curr_column_name += self.data[0][curr_index]
            else:
                if len(curr_column_name) > 0:
                    self.column_names[(prev_index, curr_index)
                                      ] = curr_column_name
                    self.is_column_area[prev_index]=1
                    self.is_column_area[curr_index-1]=1
                    curr_column_name = ""
        if len(curr_column_name)>0:
            last=len(self.data[0])
            first=len(self.data[0])-len(curr_column_name)
            self.is_column_area[first]=1
            self.is_column_area[last]=1
            self.column_names[(first,last)]=curr_column_name
        print(self.column_names)
        print(self.is_column_area)
        self.data=self.data[1:]

    def __check_edges(self, edge, row, data_point):
        """This function checks if a number is leaking out
        of their columns"""
        print("Yes it is passing:",data_point)
        check_whats_passing=data_point
        left_leak = ""
        right_leak = ""
        bad_data=False
        try:
            left_edge=self.data[row][edge[0]-1]
            right_edge=self.data[row][edge[1]]
            
        except IndexError:
            print("Exception", row, edge[0],edge[1])
            return ""
        if left_edge != " " and self.data[row][edge[0]]!=" ":
            for i in range(edge[0]-1, -1, -1):
                if self.data[row][i]==" ":
                    break
                if i in self.is_column_area:
                    bad_data=True
                    break
                left_leak += self.data[row][i]
        if right_edge != " " and self.data[row][edge[1]-1]!=" ":
            for i in range(edge[1], len(self.data[row])):
                if self.data[row][i]==" ":
                    break
                if i in self.is_column_area:
                    bad_data=True
                    break
                right_leak += self.data[row][i]
        left_leak = left_leak[::-1]
        data_point = left_leak+data_point
        data_point += right_leak
        if bad_data:
            print("Bad data: ", data_point)
            print("left edge:",left_edge)
            print("right edge:",right_edge)
            print("Og value:",check_whats_passing)
            print("Length of og value:",len(check_whats_passing))
            data_point=""
        #print("right_leak", right_leak)
        return data_point

    def add_in_dict(self, key, value):
        """This function adds corresponding keys and values
        in the transformed data dictionary
        """
        if key not in self.transformed_data:
            self.transformed_data[key] = [value]
        else:
            self.transformed_data[key].append(value)

    def map_values_to_columns(self):
        """This function maps all values to their respective columns
        while handling any missing or incorrect data type values
        """
        self._get_column_indexes()
        for curr_index, data in enumerate(self.data):
            for keys,column in self.column_names.items():
                start, end = keys[0], keys[1]
                data_point = data[start:end]
                data_point = self.__check_edges(
                        keys, curr_index, data_point)
                data_point = data_point.strip()
                if data_point != '':
                    self.add_in_dict(column, data_point)
                else:
                    self.add_in_dict(column, "NA")
        for items in self.transformed_data.items():
            print(items[0], "  :  ", items[1])


def main():
    """This is the main function"""
    data = DataExtractor("data/football.dat")
    data.map_values_to_columns()


if __name__ == "__main__":
    main()
