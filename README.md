## Feature Selection and Classification on Madelon Dataset

### Domain and Data

A synthetic dataset that was created based on UCI's Madelon dataset (https://archive.ics.uci.edu/ml/datasets/Madelon)
This dataset contains 5000 features and 220,000 rows (1.1 billion data points) whereas only 50 features contain useful information


### Problem Statement

This porject is to apply machine learning techniques to identify important features and then use these techniques to do prediction on the entire set. 

### Data Manipulation

Due to the size of the dataset, I had to built model on randomly selected subsets of the data. 
- Subset 1: 0.1% of the data
- Subset 2: 0.5% of the data
- Subset 3: 1% of the data
- Subset 4: 5% of the data


### Tasks

#### Featuer Engineering
- Use ANOVA for feature selection to select top 1000 features

#### Benchmark Modeling  
- Build naive K-Neighbors and Logistic Regression benchmark models 
- Use all 4 different size of data subsets

#### Feature Importance:     
- Create  feature selection (Select K Best/ PCA) pipelines
- Use feature selection / dimension reduction to reduce the dataset to a manageable size then use conventional methods

#### Implement Final Model:      
- Present best model and apply to larger (or all) data subset
  


### More Details can be found in /doc/MachineLearning_MadelonDataset.pdf
