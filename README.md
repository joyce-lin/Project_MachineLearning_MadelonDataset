# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 3: Feature Selection + Classification

### Domain and Data

This week, you've learned about access and utilizing remote databases, and more advanced topics for conducting logistic regression, selecting features, and building machine learning pipelines. Now, let's put these skills to the test!

You're working as a data scientist with a research firm. You're firm is bidding on a big project that will involve working with thousands or possibly tens of thousands of features. You know it will be impossible to use conventional feature selection techniques. You propose that a way to win the contract is to demonstrate a capacity to identify relevant features using machine learning. Your boss says, "Great idea. Write it up." You figure that working with a [Madelon](https://archive.ics.uci.edu/ml/datasets/Madelon)-style synthetic dataset is an excellent way to demonstrate your abilities. 

A data engineer colleague sets up a remote PostgreSQL database for you to work with upon which is loaded a massive dataset. You can connect to that database at `54.200.77.93:5432` to database `madelon` with user `postgres` and password "`postgres`". 

### Problem Statement

Your challenge here is to use machine learning techniques to identify important features and then use these techniques to do prediction on the entire set. 

### Solution Statement

Your final product will consist of:

1. A prepared report
2. A series of Jupyter notebooks to be used to control your pipelines

### Tasks

#### Data Manipulation

You should do substantive work on successively larger randomly selected subsets of the data. 

- Subset 1: .01% of the data
- Subset 2: .1% of the data
- Subset 3: 1% of the data
- Subset 4: 10% of the data
- Subset 5: 100% of the data

##### Prepared Report

Your report should:

1. be a pdf
2. present an analysis of data footprint of each subset and how it impacts your infrastructure
   - e.g. `%whos`
3. include EDA of each subset 
   - EDA needs may be different depending upon subset or your approach to a solution
4. present results from Step 1: Benchmarking
5. present results from Step 2: Identify Salient Features
6. present results from Step 3: Feature Importances
6. present results from Step 4: Build Model

##### Jupyter Notebook, Data Footprint and EDA 

- study the size in memory of the data for each subset
- present some sort of visualization of the data footprint
- perform EDA on each set as you see necessary

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
   
##### Jupyter Notebook, Step 4 - Build Model
- Implement your final model

---

### Requirements

- Many Jupyter Notebooks
- A written report of your findings that detail the accuracy and assumptions of your model.

---

### Suggestions

- Document **everything**.


