## Learning Models comparison to estimate the graduation rates of students based on census attributes
**Author:** Guduguntla Vamshi
| Affiliation:North Carolina State University, Raleigh , NC
| email: gudugu@ncsu.edu
| date: Nov 2015

#### 1.Abstract
The aim of this paper is to develop a predictive model for the graduation percentage of an individual student. The data-set which contains the reported percentages of around 9K students all over the United States. The model is developed by first screening out the unimportant variables from the given variable set (~600 variables) to discover which covariates have the most predictive power from the set. Two predictive model are proposed, one linear and another non-linear and their performances are compared using k-fold cross-validation technique.

#### 2.Introduction
This paper is produced as a partial requirement of the course ST 810: Big Data by Dr.Reich at Statistics Dept.,NCSU. The data-set consistis of predictor variables which are overlapped data of the census department with the location attributes of the school a student has attended. To meet the GradNation Campaign goal of 90% graduation rate by 2020, the attributes such as  Income, demographics, family dynamics and zip code which can play a significant part in a student’s ability to graduate. Using the data, an exploration is performed with linear and non-linear predictive techqniques to come up with a fit.

#### 3.Methods

**3.1.Sure Independence Screening of predictors**
The data has around 600 covariates trying to explain the graduation percentage(~9000 observations). I have employed the Sure independence screening by making use of Correlation values ( -1 to +1 scale) of the response with predictors. Therefore, screening out the variables which showed little or no effect(correlation here) on the graduation .By looking at the predictors qualifying in the first quintile(20 th percentile) are chosen to be the ones with highest predictive power from the remaining batch.

**3.2.Dimensional redcution by Principal Components**
The variables obtained post Sure Independence Screening are check for multi-collinearity. By performing this check, the covariates which are dependednt are screenend out.Thereby leaving us with the ones, which could explain the most possible variance in the least dimensional space. Principal components are calculated by the computing eigen values for individual dimensions.

**3.3 Linear Model - Linear Regression**

In practice, we often seek to select a distribution (model) corresponding to our data.The parameters estimates are defined and computed for the set of observations.Below is the working for parameter estimation by  maximizing the likelihood.

![screen shot 2015-11-10 at 11 33 56 am](https://cloud.githubusercontent.com/assets/10588000/11068381/ff74f56a-879e-11e5-8edb-b61db0deab40.png)

**3.4 Non-Linear Model - Random Forests**

Random forests are a combination of tree predictors such that each tree depends on the values of a random vector sampled independently and with the same distribution for all trees in the forest.Random forests are an effective tool in prediction. Because of the Law of Large Numbers they do not overfit. Injecting the right kind of randomness makes them accurate regressors

#### 4.Results:
**Important Features**
Using the above mentioned techniques, some of the important features are as given below. 

```
Aggregate_HH_INC_ACS_08_12 - Aggregate Household income
NH_White_alone_CEN_2010 - Non hispanic white students
pct_No_Plumb_ACS_08_12 - housing units that do not have complete plumbing facilities
Med_HHD_Inc_ACS_08_12 - Median  household income for the tract
MrdCple_Fmly_HHD_ACS_08_12 - Married-couple family households
pct_Tot_Occp_Units_ACS_08_12 - % housing units that are classified as the usual place of residence 
```
The quantitative data, though not all-encompassing, has the indicators for the graduation rate predictions. However, we could get a deeper insight with certain qualitative indicator like education level of the parents,etc.

#### 5.Predictions

While the training data is split into k-1 folds for training and one fold  for testing, the parameter estimates are recorded in trainig set and and fitted to the one fold test set. For the the given observations, the recorded Mean Squared Error is reported below
```
                                    | Model                     | Mean Squared Errror  |
                                    |---------------------------|----------------------|
                                    | Ordinary Least Square     | 109.34               |
                                    | Lasso                     | 109.35               |
                                    | Random Forests            | 109.68               |
```

Using k-fold cross-validation reports the consistency in the MSE computed. The above calculated MSE are the means of the Mean squared errors of each fold. Looking at the results, Linear fit seems to be the most suited to the given data and has the accuracy closer to Random forests. Therefore, a OLS fit would be the preferred choice to fit the data for its simplicity and interpretability.
