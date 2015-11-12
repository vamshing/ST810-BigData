# Multiple Testing

#### 1. Overview & History

While performing a large number of statistical tests, some will have p-values less than the significance level purely by chance, even if all of the null hypothesis are really true. This is corrected by using Controlling the Family wise error rate and the False Discovery Rates. We present two methods to address this problem - bonferroni adjustment and Benjamini-Hochberg procedure and demonstrate the ideas.

#### 1.1 The problem with multiple comparisons:

Say you have a set of hypotheses that you wish to test simultaneously. The first idea that might come to mind is to test each hypothesis separately, using some level of significance α. At first , this doesn’t seem like a bad idea. However, consider a case where you have 40 hypotheses to test, and a significance level of 0.05. What’s the probability of observing at least one significant result just due to chance?

```
P(at least one significant result) = 1 − P(no significant results)
                                   = 1 - (1-0.05)^20
                                   ~ 0.64

P(at least one significant result) = 1 − P(no significant results)
                                   = 1 - (1-0.05)^40
                                   ~ 0.88
```

So, with 40 tests being considered, we have a 88% chance of observing at least one significant result, even if all of the tests are actually not significant. In genomics and other biology-related fields, it’s not unusual for the number of simultaneous tests to be quite a bit larger than 40 and the probability of getting a significant result simply due to chance keeps going up.

Methods for dealing with multiple testing frequently call for adjusting α in some way, so that the probability of observing at least one significant result due to chance remains below your desired significance level.

#### 1.2 Line of research:

- Benjamini Y, Hochberg Y. Controlling the false discovery rate: a practical and powerful approach to multiple testing. Journal of the Royal Statistical Society B. 1995;57:289–300















Guduguntla Vamshi <gudugu@ncsu.edu>
Jianhong
Dan <jchang7@ncsu.edu  dchen9@ncsu.edu
