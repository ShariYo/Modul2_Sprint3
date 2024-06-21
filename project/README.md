
# Fast Food Market and Cookie Cat game analysis

This is a study on Red Wine Quality with a given dataset of different chemical parameters of Wine. Purpose of the project is to understand and analyse which parameters impacts Wine Quality the most.


## Data source

Given data source can be found at Kaggle with the two links provided below:

  **Red Wine Quality**  

  https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009/data



## Main functions/libraries used for data analysis:  

### Libraries:  
- numpy;
- pandas;
- matplotlib.pyplot;
- seaborn;
- functions_sandbox (personal set of functions);
- scipy.stats;  
- statsmodels.api as sm

### Plots:
- sns.histplot();
- sns.heatmap();
- sns.barplot();
- sns.regplot();
- sns.lineplot();
- sns.pairplot();
- sns.scatterplot()
### Files:
- redwine.csv;
- main.ipynb;
- functions_sandbox.py

## Summary
 
Given dataset of Red Wine Quality was analysed and the results presented in a  
Jupyter Notebook.  
- The dataset have 12 with various variables;  
- Quality variable is the main one to check dependence in other features, try different regression models. Despite in is int Dtype, quality is categorical type feature;  
- Quality levels data distribution seems normal with 5 and 6 level having most of the data points;  
- Boxplots were plotted for each variable by quality and checked which features were meaningful to analyse deeper. Four variable were selected: volatile acidity, citric acid, sulphates and alcohol percentage;  
- After fitting linear regression model, alcohol percentage seemed to have the most meaningful correlantion with wine quality;  
- Data of 20% hold-out was also analysed and results are provided in main.ipynb;  
- Further investigation contigued with transformed dataset only for alcohol and quality where quality feature values was transformed to Binary and Logistic Regression was analysed;  
- Logistic regression seemed to fit more properly that linear.  

**What could have been done more**: 
- H0 hypothesis with different features could have been analysed;  
- Try more regression models;  
- Try multiple regression model plotting;  
- Functions_sandbox.py file functions could be updated, increased automation quality.

