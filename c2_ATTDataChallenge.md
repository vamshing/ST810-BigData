## Learning Models to estimate the graduation rates of students based on census attributes
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
The data has around 600 covariates trying to explain the graduation percentage(~9000 observations). I have employed the Sure independence screening by making use of Correlation values (### -1 to +1 scale) of the response with predictors. Therefore, screening out the variables which showed little or no effect(###correlation here) on the graduation .By looking at the predictors qualifying in the first quintile(20 th percentile) are chosen to be the ones with highest predictive power from the remaining batch.

**3.2.Dimensional redcution by Principal Components**
The variables obtained post Sure Independence Screening are check for multi-collinearity. By performing this check, the covariates which are dependednt are screenend out.Thereby leaving us with the ones, which could explain the most possible variance in the least dimensional space. Principal components are calculated by the computing eigen values for individual dimensions.

**3.3.The Grouped-Lasso Regression**
Working with high-dimensional learning problems require specific assumption which would lead to greater accuracy. Now, we have the co-variated groups, with the pointindex grouping as discussed above. The Group-Lasso technique(assuming sparsity) is employed to fit the data which is implemented via generalized gradient descent. 
The lasso approach works for the case where p>>n by bounding the l1 norm of the solution. It was proposed by [2.Tibshirani [1996]](http://statweb.stanford.edu/~tibs/lasso/lasso.pdf). However, the grouped lasso takes into account the m divided groups of covariates. For this problem, I have considered the "sparse-group lasso" as given by the definition below:
![screen shot 2015-09-24 at 11 44 20       am](https://cloud.githubusercontent.com/assets/10588000/10078205/a93f28b2-62b1-11e5-8b06-7c3cbe2cf1dc.png)

where  α ∈ [0, 1] — a convex combination of the lasso and group lasso penalties (α = 0 gives the group lasso fit, α = 1 gives the lasso fit).

The above model is implemented via co-ordiante descent algorithm.

#### 4.Results:
**4.1.Model Fit**
Using k-fold cross-validation, the model is trained and tested to yield Mean squared error for each set of observations. Using the parameter estimates, the model is used to fit the known covaraites with unknown response. 

**4.2.Mean Squared Error**
While the training data is split into 70 observations for training and 30 observation for testing, the parameter estimates are recorded and fitted to the remaining 100 test set. For the 100 observations, the recorded Mean Squared Error is 6.32.

**4.3.Top ten predicted subjects by musical ability**
According to the predictions, below is the table for the subjects ranking on predicted musical ability.

                                    | Subject | Predicted Musical ability |
                                    |---------|---------------------------|
                                    | 182     | 14.938                    |
                                    | 135     | 13.054                    |
                                    | 136     | 12.991                    |
                                    | 161     | 12.911                    |
                                    | 198     | 12.768                    |
                                    | 145     | 12.715                    |
                                    | 180     | 12.686                    |
                                    | 111     | 12.648                    |
                                    | 166     | 12.25                     |
                                    | 126     | 12.19                     |


#### 5.Predictions





