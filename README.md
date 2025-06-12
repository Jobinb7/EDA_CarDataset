Project: Exploratory data analysis of a car dataset using python

Data : Dataset is taken from kaggle(https://www.kaggle.com/datasets/shalwalsingha/cars-ds-final)
       This data set contains the automotive data.
       
       orginal data: https://drive.google.com/file/d/1ET_9EKbCO7702KIBSFDZur44nOiNQE1A/view?usp=sharing
       
       cleaned data: https://drive.google.com/file/d/1819qAQzBKXPDDd5P8EnyIa8-nnX0b13N/view?usp=sharing

 🗂️ Project Structure:

 The  folder inside this repository contains the python script ,various graphs and requirements.txt

 📈 Exploratory Steps:
 1) Data loading and cleaning:The orginal csv file was cleaned and loaded into a local host MySQL database and created a  table and
                              the data is loaded into the python platform by making connection between the local host MySQL database .

 2) Find the missing values

 3)  Grouped the data based on categorical and bunerical variables

 4)  Univariate analysis
 5)  Multivariate nalysis
 6)  Normality tests
📊 Key Insights

The intial dataset contain 1262 rows and 129 columns.After determining the missing values in each columns by "df.isnull().sum()" and by plotting Missing values per columns,the columns which is having the more than 40 percentage missing values are dropped.
![Alt Text](https://github.com/Jobinb7/EDA_CarDataset/blob/90862e9ca25d1d6c4f9591949a15ac1d0fca2bbf/percentage_of_missing.png)
There fore, 48 columns got  removed from the main dataset.Then the  data set contains 64 categorical columns and 17 numerical columns.Using describe() function the distribution of the numerical columns got understoood. 
The following are the distribution of the numerical variables graphically.
![Alt Text](https://github.com/Jobinb7/EDA_CarDataset/blob/465e7fd422cb223a5d81c904c1bcd280fc72e707/Histogram_plot_EDA.png)

The following are the ditribution of the categorical variables graphically
![Alt Text](https://github.com/Jobinb7/EDA_CarDataset/blob/de35ef49f86e3d52ae6a8ed77cffc627461ee4b4/categorical_distribution.png)
.There are 20 columns which is lacking in variability ,cannot considered for modelling. The following graph was used to  determine this 
![Alt Text](https://github.com/Jobinb7/EDA_CarDataset/blob/79dd10cca7499dc9556210f5ba120ff0eca11fd1/most_frequent_value_ratio.png)


 There are 25 columns ,which has atleast 4 different values.Because of the variability in the data ,these columns can be considered for modelling .This is determined  graphically.
 
 The relationship between all the numerical variables are determined by correlation matrix.The following is the heat map graph shows the postive correlation,
 negative correlation .
 ![Alt](https://github.com/Jobinb7/EDA_CarDataset/blob/c3426ffdd19e2c0d02fe0f2e8f2562d03f4ec8ae/Correlation_matrix.png)
 None of the 16 numerical variables folows normal distribution as confirmed by shapiro wilk test.
 Management of missing values are not done because my aim was to predict  resale value of the car and those droppped variables are not useful for the same.



    
