# first assignment

In this assignment, you will create functions to evaluate the log likelihood and gradient functions
for a logistic regression model with one covariate. The likelihood function is

i=1t to n
 II (exp[Yi(β1 + Xiβ2)]) / (1 + exp(β1 + Xiβ2))

where Yi ∈ {0, 1} and Xi ∈ R are the binary response and covariate, respectively, for observation i.
You should create four functions: the log likelihood and gradient function in R and Rcpp. All four
functions should have inputs: beta (2-vector), Y (n-vector), and X (n-vector). The log likelihood
functions should return a scalar, the gradient functions should return a 2-vector.
