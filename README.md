# Data Munging (Using SOLID)

 ## Introduction
This project is meant to extract and analyze data from given files, The user can input the file path in the program.

## How to install
1.  **Clone the repository:**

		git clone https://github.com/the-void-century/Data_Munging.git

2. **Install Python:**

		sudo install python

## How to use

- Run the `calculator.py` program, You'll get a prompt to enter the path of the file, enter the absolute or the relative path of the file.
- Enter the columns for which you want the minimum difference for and then enter the attribute you want to see of that given record.

## Classes
- **Extractor:** This class is solely responsible for extracting the data from given dat files. It accepts data directly, The two functions that the user needs to keep in mind while using this class are:
	1. `.set_data()`: This function sets the data path from which the data will be extracted.
	2. `.map_values_to_columns()`: This function will transform and return the data extracted in a 2-dimensional dictionary.

- **Analyzer:** This class accepts transformed data and returns minimum difference of two values in any two specified columns.
	1. `.set_data()`: This function will accept transformed data and set it as the data for this instance of the class.
	2. `.min_diff()`: This function accepts three arguments: `Column1`,`Column2`,`Answer_column` and returns the corresponding value of `Answer_column` where the difference between `Column1` and `Column2` is minimum

- **Calculator:** This is our main class which connects the Analyzer and the Extractor class. This class accepts the Extractor and Analyzer objects in its constructor.
	1. `.calculate()`: This function accepts `Column1`, `Column2` and `Answer_column` and further passes it to the `min_diff` function of the Analyzer object.


