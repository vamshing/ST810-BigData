# Investigating BootStrap Intervals for LASSO

** Description ** : The purpose of this study is to simulate the properties of Bootstrap Confidence intervals for LASSO.


**Method** : 
- Generated m(=1000) data-sets with p(=10,100,1000) samples with 5 covariates.
- Calculating the bootstrap confidence interval 
- Including a flag which would check for th true Beta value present in the Confidence interval or not
-  Computing the probability given by the formula : #Cells with Beta present in CI/Total CI's generated.
- This is repeated and analyzed for the cases p=10,100,1000

**Results**:

***1.p=1000 samples**

beta1    0.98
beta2    0.98
beta3    0.98
beta4    0.99
beta5    0.94

***2.p=100 samples**

beta1    0.96
beta2    0.96
beta3    0.99
beta4    0.99
beta5    0.94

***3.p=10 samples**





