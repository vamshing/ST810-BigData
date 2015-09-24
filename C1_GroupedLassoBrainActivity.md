## A Predictive Model to estimate subject's musical ability based on brain activity data.
**Author:** Guduguntla Vamshi
  affiliation:North Carolina State University, Raleigh , NC
  email: gudugu@ncsu.edu
date: January 2014

**Abstract:** The aim of this paper is to develop a Statistical model to predict te musical ability of an individual subject. We are given a data-set which contains the response of 200 subjects at different locations in the brain space. The space forms a 3D area with (u,v,w) spanning voxels in the brain. The predictive model proposed, uses a form of penalized-regression called Group Lasso Technique. The brain voxels are grouped together using a novel method called, the pointindex estimation, which groups the brain hot-spots together in producing the response.The results are compared with Ordinary Least Squares and Ridge Regression, the current standard methods of penalized regression to demonstrate the efficacy of the proposed model.

#### 1.Introduction
This paper is produced as a partial requirement of the course ST 810: Big Data by Dr.Reich at Statistics Dept.,NCSU. The data-set consistis of predictor variables which record the brain response to test the musical ability. The dimensional space of the brain {u,v,w} is uniformly mapped accross 20x20x20 space, producing 8,000 voxels in the region for an individual subject.With n=100, the total number of subjects, the data-set has the musical ability index as the response variable.The goal here is to build a statistical model using the responses, be able to predict the musical ability of a test subject with known response in the brain voxels.

#### 2.Methods

**2.1.Sure Independence Screening of predictors**
The data has 8,000 response variable as a product of 20 co-ordinate unites in each of {u,v,w} directions. This is the case for p > n, with few knwon observations(n=100). I have employed the Sure independence screening by making use of Correlation values (### -1 to +1 scale) of the response with predictors. Therefore, screening out the variables which showed little or no effect(###correlation here) on the musical ability.By looking at the predictors which are atleast correlated by 0.10(on the absolute scale) are chosen to be the ones with highest predictive power from the remaining batch.

**2.2.Clustering the predictors**
The screened brain location variables {u,v,w} pairs have the spatial distribution in a clustered manner. While it is observed that the musical ability in concentrated at certain parts of the brain, I have considered clustering of the points so that they can be grouped. The method used to cluster the voxels is pointindexing which is summarized below. Each voxel's index is given a rank by the formula:
```
P(u{a},v{b},x{c}) = n(P(u{j},v{k},x{l}))
where a,b,c is the voxel index to be computed.
and n(x) denotes the count of x's.
j,k,l E {1,2,.....,20}
```
Once the index of each voxel is computed, we sort them in the order of highest pointindex, and assign the groups. The groups are determined by the drawing a cluster-sphere around each point. The groups are assigned by the following pseudo-code:
```
set group to 1
u{a},v{b},x{c} where is a,b,c is the point with highest pointindex
when u{a},v{b},x{c} - u{j},v{k},x{l} < 5.0: (j,k,l E {1,2,.....,20})
  assign u{a},v{b},x{c} and u{j},v{k},x{l} to group 
increment group by 1
set u{a},v{b},x{c} where is a,b,c is the point with next highest pointindex
repeat
```
The formed clusters are bigger around the points with higher pointindex. This rebutts the fact about the efficacy of using the pointindex to figure out the brain-hotspots which correlated highly with the musical ability of the subject.

**2.3.The Grouped-Lasso Regression**
Working with high-dimensional learning problems require specific assumption which would lead to greater accuracy. Now, we have the co-variated groups, with the pointindex grouping as discussed above. The Group-Lasso technique(assuming sparsity) is employed to fit the data which is implemented via generalized gradient descent. 
The lasso approach works for the case where p>>n by bounding the l1 norm of the solution. It was proposed by [2.Tibshirani [1996]](http://statweb.stanford.edu/~tibs/lasso/lasso.pdf). However, the grouped lasso takes into account the m divided groups of covariates. For this problem, I have considered the "sparse-group lasso" as given by the definition below:
![screen shot 2015-09-24 at 11 44 20       am](https://cloud.githubusercontent.com/assets/10588000/10078205/a93f28b2-62b1-11e5-8b06-7c3cbe2cf1dc.png)

where  α ∈ [0, 1] — a convex combination of the lasso and group lasso penalties (α = 0 gives the group lasso fit, α = 1 gives the lasso fit).

The above model is implemented via co-ordiante descent algorithm.

#### 3.Results:
**3.1.Model Fit**
Using k-fold cross-validation, the model is trained and tested to yield Mean squared error for each set of observations. Using the parameter estimates, the model is used to fit the known covaraites with unknown response. 

**3.1.Mean Squared Error**
While the training data is split into 70 observations for training and 30 observation for testing, the parameter estimates are recorded and fitted to the remaining 100 test set. For the 100 observations, the recorded Mean Squared Error is 6.32.

**3.1.Top ten predicted subjects by musical ability**
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


#### 4.References
1. [A SPARSE-GROUP LASSO NOAH SIMON, JEROME FRIEDMAN, TREVOR HASTIE, AND ROB TIBSHIRANI](http://web.stanford.edu/~hastie/Papers/SGLpaper.pdf) 
2. [Regression Shrinkage and Selection via Lasso : Tibshirani [1996]](http://statweb.stanford.edu/~tibs/lasso/lasso.pdf)





