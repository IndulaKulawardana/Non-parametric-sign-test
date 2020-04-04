#### Sign Test for small sample  

#### Example 1: 
A Bank manager claims that the median number of customer per day is no more than 750.  
The number of bank customers per day for 16 randomly selected days are given in the Sample_1.csv file.
The sign test is used to test the Bank Manger's claim at 5% significance level. 
Since sample size is less than 50 and distribution of data is not normally distributed, 
the algorithm written for sign test for small sample size is used.

#### Sign Test for large sample

#### Example 2:  
A Company Manager needs to figure out whether the median number of weekly sales 
is less than 5120 or not. Number of Sales in the company is given in the Sample_2.csv file. 
The sign test is used to test the Manger's claim at 5% significance level.
Since sample size is greater than 30, the algorithm written for sign test for large sample size is used.  

#### Sign Test for paired sample (Small in size)

#### Example 3: 
A golf instructor is interested in determining if her new technique for improving players’ golf scores is effective. She randomly selected 10 new students. 
She records their 18-hole scores before learning the technique and then after having taken her class. 
The sign test is used to test the golf instructor's claim at 5% significance level. 

<<<<<<< HEAD
Note: The algorithm written for sign test for small sample size is used after taking difference between relevant two 
columns provided in the Sample_3.csv file. 


#### Guidelines 
a) Install python 3x, pip

b) Create a virtual environment. 
   In command shell/terminal, go to your project’s directory and run venv using following command.
   
   'python -m venv venv'
   
=======
Note: The algorithm written for sign test for the paired samples is used after taking difference between relevant two 
columns provided in the Sample_3.csv file. 

#### Guidelines 
a) Install python 3x and pip
 
b) Create a virtual environment.
   In command shell/terminal, go to your project’s directory and run venv using following command.
   
   'python -m venv venv'

>>>>>>> 5ee73e2c2064e02557b95b8dea8134f80e66aa4d
c) Before starting installing packages in the created virtual environment, you need to 
   activate the virtual environment using following command.

   'venv\Scripts\activate'
   
d) Run the following command to install requirements 
    
   'pip install -r requirements.txt'

e) Follow the below steps to execute Sign Test for your own data set to test your claim based on Median of the distribution of data. 

- Input your sample data file (in csv format) into input folder
- Substitute required parameters in config.py file
- Create a folder and name the folder as Output
- Run run.py file (Results are saved as html file(s) in the Output folder)
