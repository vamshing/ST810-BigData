### Simulating Gaussian regression - for covariance parameters

10/21/2015 by Guduguntla Vamshi <gudugu@ncsu.edu>

####**Summary**

A **Generalized Additive Model** is fitted with the log number of deaths on the day as the (approximately Gaussian) response and 
the subset of covariates. The primary scientific interest is to determine if the daily values of the four air pollutants 
ozone, SO2, NO2, and CO are associated with daily mortality. 
**The dataset** also includes the one-day lag of each pollutant.Other covariates are checked for the pollutants 
associated with the response, if they have non-linear effects, and whether the pollutants interact with each other.

####**Methods**

**1.Non-Linear Effects:**
  - Residuals of the linear model are computed and plotted with the covariates. The plots are used to analyze the non-linearity 
    of the covariates with the residuals, and decided on the estimated effect.

**2.Pollutants/Covariants association with response/mortality:**
  - Once the covariates with non-linear effects are determined, the non-linear covariates are fitting using loess function
    and run through a parametric Analysis of Variance. The p-values are checked for the null hypothesis being true.

**3.Interactions between the Pollutants/Covariants:**
  - An interaction model is fit between the possible combinations of significant variables using loess funciton as defined by
    non-linearity. The p-values are checked for the interaction term of the null hypothesis being true. 

**4. Selection of model/function in GAM:**
  For this purpose, the two functions: Local Polynomial Regression Fitting (LOESS) and Spline functions are considered
  Both the models are fitted and model with lowest AIC is used to chose the model. 
  **Reasoning**: AIC is a goodness of fit measure that favours smaller residual error in the model, but penalises for 
  including further predictors and helps avoiding overfitting. In the set of models model 1 (the one with the lowest AIC) 
  may perform best when used for prediction outside the dataset.


####**Results**

**1.Non-Linear Effects of Pollutants:**

[Ozone - Non-Linear]<img src="https://cloud.githubusercontent.com/assets/10588000/10654345/2362d5c2-7837-11e5-9f32-80add480f546.png" width="200"> [SO2 - Non-Linear]<img src="https://cloud.githubusercontent.com/assets/10588000/10654345/2362d5c2-7837-11e5-9f32-80add480f546.png" width="200">

[NO2 - Linear]<img src="https://cloud.githubusercontent.com/assets/10588000/10654354/2fca958e-7837-11e5-9dcb-b23c8cb62fe5.png" width="200"> [CO - Non-Linear]<img src="https://cloud.githubusercontent.com/assets/10588000/10654355/30e5f990-7837-11e5-839a-5a9adae22ce0.png" width="200">


**2. Pollutants association with response:**

```R 
Anova for Parametric Effects
                 Df Sum Sq Mean Sq   F value    Pr(>F)    
lo(data$O2)     1.0 149138  149138 1169.1885 < 2.2e-16 ***
lo(data$SO2)    1.0   2071    2071   16.2348 5.677e-05 ***
data$NO2        1.0    148     148    1.1571    0.2821    
lo(data$CO)     1.0   5882    5882   46.1118 1.244e-11 ***
Residuals    5099.2 650436     128      
```
Fitted with the **Generalized Additive Model** with the loess, **turns out that NO2 has no association with response.**

**3.Testing for Interactions:**

  3.1 Interaction between O2 and SO2 - Significant
  
````lo(data$O2, data$SO2)     6.2 10.036 2.794e-11 .***````
  
  3.2 Interaction between O2 and CO  - Not Significant
  
  ````lo(data$O2, data$CO)     5.8  1.414 0.20707````
  
   3.3 Interaction between SO2 and CO - Not Significant
   
````lo(data$SO2, data$CO)     6.1  1.645 0.1291````

**4.Selecting the final model:**
  Model 1 : fit4 <- ```` gam(data$Deaths~lo(data$O2)+lo(data$SO2)+data$NO2 +lo(data$CO)+lo(data$O2,data$SO2)) ````
  ```` AIC: 39329.51 ````
  
  Model 2 : fit <- ```` gam(data$Deaths~s(data$O2)+s(data$SO2)+data$NO2 +s(data$CO)+lo(data$O2,data$SO2)) ````
  ```` AIC: 39326 ````


####**Conclusion**

The chose model is Generalized Additive model with spline, inlcuding the significant interaction between the covariates
O2 and SO2. The method used to chose the model are AIC, Non-linear relationship of the covariate, log transform of response
variable and ANOVA for parametric effects.**Model 2 is chosen to be the final model** 


