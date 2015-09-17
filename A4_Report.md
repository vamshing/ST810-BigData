# Investigating BootStrap Intervals for LASSO

**Description** : The purpose of this study is to simulate the properties of Bootstrap Confidence intervals for LASSO.


**Method** : 
- Generated m(=1000) data-sets with p(=10,100,1000) samples with 5 covariates.
- Calculating the bootstrap confidence interval 
- Including a flag which would check for th true Beta value present in the Confidence interval or not
-  Computing the probability given by the formula : #Cells with Beta present in CI/Total CI's generated.
- This is repeated and analyzed for the cases p=10,100,1000

**Results**:

**1.p=1000 samples**

beta1    0.98
beta2    0.98
beta3    0.98
beta4    0.99
beta5    0.94

**2.p=100 samples**

beta1    0.96
beta2    0.96
beta3    0.99
beta4    0.99
beta5    0.94

**3.p=10 samples**

beta1    0.99
beta2    0.98
beta3    0.99
beta4    0.99
beta5    0.98

**Code Snippet**

def bootstrap_lasso(m):
    np.random.seed(m*212222)
    n_samples, n_features = 10, 5
    X = np.random.randn(n_samples, n_features)   
    coef = 3 * np.random.randn(n_features)
    inds = np.arange(n_features)
    np.random.shuffle(inds)
    coef[inds[10:]] = 0  # sparsify coef
    y = np.dot(X, coef)    
    lasso = Lasso(alpha=0.1)
    y_pred_lasso = lasso.fit(X, y)   
    global r1
    r1 = lasso.coef_
    def my_function2(i):
        lasso = Lasso(alpha=0.1)
        lasso.fit(X[i],y[i])
        return lasso.coef_
# 95% Confidence Interval 
    global ci
    ci = boot.ci(np.arange(len(X)), statfunction=my_function2, alpha=0.01, n_samples=1000, method='pi')    
    table.loc[m,'beta1'] = int(r1[0] > ci[0][0] and r1[0] < ci[1][0])
    table.loc[m,'beta2'] = int(r1[1] > ci[0][1] and r1[1] < ci[1][1])
    table.loc[m,'beta3'] = int(r1[2] > ci[0][2] and r1[2] < ci[1][2])
    table.loc[m,'beta4'] = int(r1[3] > ci[0][3] and r1[3] < ci[1][3])
    table.loc[m,'beta5'] = int(r1[4] > ci[0][4] and r1[4] < ci[1][4])




