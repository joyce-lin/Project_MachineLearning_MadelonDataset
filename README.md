## Feature Selection and Classification on Madelon Dataset

### Domain and Data

A synthetic dataset that was created based on UCI's Madelon dataset (https://archive.ics.uci.edu/ml/datasets/Madelon)
This dataset contains 5000 features and 220,000 rows (1.1 billion data points) whereas only 50 features contain useful information


### Problem Statement

This porject is to apply machine learning techniques to identify important features and then use these techniques to do prediction on the entire set. 

### Data Manipulation

Due to the size of the dataset, I had to built model on randomly selected subsets of the data. 
- Subset 1: .1% of the data
- Subset 2: .5% of the data
- Subset 3: 1% of the data
- Subset 4: 5% of the data


### Tasks
1. Data EDA:      Use ANOVA for feature selection to select top 1000 features
2. Benchmark Modeling:     Create K-Neighbors and Logistic Regression benchmark models 
3. Feature Importance:     Create  feature selection (Select K Best/ PCA) pipelines
                           - Use feature selection / dimension reduction to reduce the dataset to a manageable size then use conventional methods
4. Implement Final Model:      Present best model and apply to larger data subset






##### Jupyter Notebook, Step 1 - Benchmarking
- build pipeline to perform a naive logistic regression as a baseline model
- optionally, run one or more additional naive models e.g. decision tree, k nearest neighors, etc
- use at least three different size subsets of the data
- in order to do this, you will need to set a high `C` value in order to perform minimal regularization

##### Jupyter Notebook, Step 2 - Identify Features
- Build feature selection pipelines using at least three of these methods:
   - a Lasso model
   - SelectKBest
   - SelectFromModel
   - RFE
   - PCA
   - KernelPCA
   - SVD
- Perform each of the three on at least three subsets of data
- **NOTE**: these pipelines are being used for feature selection not prediction

##### Jupyter Notebook, Step 3 - Feature Importance
- Use the results from step 2 to discuss feature importance in the dataset
- Considering these results, develop a strategy for building a final predictive model
- recommended approaches:
    - Use feature selection to reduce the dataset to a manageable size then use conventional methods
    - Use dimension reduction to reduce the dataset to a manageable size then use conventional methods
    - Use an iterative model training method to use the entire dataset
- Implement at least one of these on at least two different size subsets of data
   



