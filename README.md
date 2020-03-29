# Overall of Data Science

from: 
1. [Marverick Lin](http://mavericklin.com)
2. [365 Data Science](https://365datascience.com/)
3. [Machine Learning Co Ban by VuHuuTiep](https://github.com/tiepvupsu/ebookMLCB)
4. Wikipedia

## What is data Science?
Multi-disciplinary field that brings together concepts from computer science, statistics/machine learning, and data analysis to understand and extract insights from data.

Two paradigms of data research:
1. **Hypothesis-Driven**: Given a problem, what kind of data do we need to help solve it?
2. **Data-Driven**: Given some data, what interesting problems can be solved with it?

The heart of data science is to always ask questions. Always be curious about the world. _What can we learn from this data and How to do it?_
____________________

## Types of Data
* **Structured**: e.g. tables, spreadsheets, or relational databases.
* **Unstructured**: e.g. blobs of text, images, audio.
* **Numerical** (quantitative): e.g. height, weight.
* **Categorical** (qualitative): e.g. race, sex, hair color.
* **Big Data**: data that contains greater _variety_ arriving in increasing _volumes_ and with ever-higher _velocity_ (3 Vs). Cannot fit in the memory of a single machine.

### Data Sources/ Fomats
**Sources**: Companies/Proprietary data, API, Goverment, Academic, Web Scraping/ Crawling.
**Formats** (most common):
1. CSV:
2. XML:
3. SQL:
4. JSON:
5. Protocol buffers:
____________________

## Main Types of Problems
Two problems arise repeatedly in data science:
1. **Classifications**: Assigning something to a discrete set of possibilites. e.g. spam or non-spam, blood type, ...
2. **Regression**: Predicting a numerical value. e.g. someones's income, next year GDP, stock price, ...
_____________

## Probability Overview
Probability is **the likelihood of an event occurring**.

### Terminology
* **Event**: Set of outcomes of an experiment e.g. event that a roll is 5, or the event that sum of 2 rolls is 7.
* **Preferred (favorable) outcomes**: They are the outcomes we want to occur or the outcomes we are interested in.
* **Sample Space (S)**: Set of possible outcomes of a experiment e.g. if tossing a dice, S= (1,2,3,4,5,6)
* **Probability of an event (X)**: It equals the _number of preferred outcomes_ over the _number of outcomes in sample space_. **P(X)=(preferred outcomes)/(sample space)**

    * We measure probability with numeric values between 0 and 1, so we like to compare the relative likelihood of events.

* **Trial**: Observing an event occcur and recording the outcome - e.g. flipping a coin and recording its outcome.
* **Experiment**: A collection of one or multiple trials - e.g. flipping a coin 20 times and recording the 20 individual outcomes.
* **Expected Value**: The specific outcome we expect to occure when we run an experiment. **E(X) = P x X**

### Independence, Conditional, Compound
* **Joint Probability**: P(A,B) = P(B |A)P(A) = P(A |B)P(B)

* **Marginal Probability**: P(A)

* **Independent Events**: A and B are independent.
    * _P(A,B) = P(A) * P(B)_
    1. P(A |B) = P(A)
    2. P(B |A) = P(B)

* **Conditional Probability**: 
    * _P(A |B) = P(A,B)/P(B)_
    1. P(A |B): Probability of A, given B has occurred.
    2. P(A,B): Probability of _prefered outcomes_
    3. P(B): Probability of _sample space_
    
* **Additive Law**: It calculates the probability of the union based on the probability of the individual sets it accounts for.
    * _P(A union B) = P(A) + P(B) - P(A,B)_
    
* **Multiplication Law**: _P(A,B) = P(B |A)P(A) = P(A |B)P(B)_
    * If event B occurs in 40% of the the time (P(B) = .4) and event A occurs in 50% of the time B occurs (P(A |B) = .5), then they would simultaneously occur in 20% of the time.

* **Bayes Theorem**: Bayes' Law helps us understand the relationship between  two events by computing the different conditional probabilities. It is often used in medical or business analysis to determine which of two symptoms affects the other one more.
    * _P(A |B) = (P(B |A) x P(A)) / P(B)_

### Probability Distributions
* **Random Variable (x)**: A variable is used to estimate uncertainty values. A random variable is either discrete or continuous.

* **Probability Function p(x)**: A function that assigns a probability to each distinct outcome in the sample space.

* **Probability Distribution**: Observing in an experiment, some values occurs more than the other. So that information can be measure by a _probability distribution_ which is depicted by a _probability function p(x)_

* **Probability Density Function (PDF)**: This is impossible to know exactly probability of a continuous random variable. So the _probability distribution_ is often based on the interval that outcomes belong to. That is depicted by _probability density function_.

* **Cumulative Density Function (CDF)**: CDF has a range from 0 to 1 and represents the sum of all the _PDF_ values up to the point we are interseted in.
___________

## Classic Statistical Distributions

A distribution is a function that shows the possible values for a variable and how often they occur. It is a _common mistake_ to believe that the distribution is the _graph_, we often use graphs to visualize the data.

### Discrete
1. **Binomial Distribution**
    
    * Measures the frequency of occurrence of one of the possible outcomes over the n trials. E.g.: Determining how many times we expect to get a heads if we flip a coin 10 coins.
    * Y ~ Bin(_n_,_p_) | Y: success rate -- n: number of trails -- p: prob of success.
    * PDF: P(Y=y) = C(y,n) * _p^y_ * _(1-p)^(n-y)_
    * Often used when trying to predict how likely an event is to occur over a series of trials.

2. **Poisson Distribution**: 
    
    * When we want to know the likelihood of a certain event occurring over a given interval of time or distance. 
    * Y ~ Po(_lambda_) | Y: a specific outcome -- lambda: a interval of time or distance.
    * Used to determine how likely a specific outcome is, knowing how often the event usually occurs. Often incorporated in marketing analysis to determine whether above average visits are out of the ordinary or not.    
    
### Continuous
1. **Normal/ Gaussian Distribution**

    * Represents a distribution that most natural events follow. E.g. often observed in the size of animals in the wilderness.
    * Y ~ N(_mean_,_var_)
    * Its graph is bell-shaped curve, symmetric and ha thin tails.
    * _68%-95%-99% rule_: 68% of probability mass fall within _1*var_ of the _mean_, 95% within _2*var_, and 99.7% within _3*var_.
    * Could be standardized to use the Z-table.
    
2. **Logistic Distribution**

    * Determine how continuous variable inputs can affect the probability of a binary outcome.
    * Y ~ Logistic(_mean_,_s_) | s: scale parameter.
    * Often used in sports to anticipate how a player's or team's performance can determine the outcome of the match.
___________

## Data Analysis
[_Data Analysis_](https://en.wikipedia.org/wiki/Data_analysis) is a process of cleaning, exploring and modeling data with the goal of discovering useful information (insights) and supporting decision-making.

In statistical applications, _DA_ can be divided into:
* **Exploratory Data Analysis**: focuses on discovering new features in the data.
* **Descriptive Statistics**: summarizes about the sample.
* **Confirmatory Data Analysis (Inferential Statistics)**: focuses on confirming or falsifying existing hypotheses.
___________

## Data Cleaning
[_Data Cleaning_](https://en.wikipedia.org/wiki/Data_cleansing) is the process of turning raw data into a clean and analyzable data set. "Garbage in, garbage out". Make sure garbage doesn't get put in.

### Errors vs. Artifacts

* **Errors**: Information that is lost during acquisition and can be recovered e.g. power outage, crashed servers.
* **Artifacts**: Systematic problems that arise from the data cleaning process. These problems can be corrected by we must first discover them.

### Data Compatibility

Data compatibility problems arise when merging datasets. Make sure you are comparing "apples to apples" and not "apples to aranges". Main types of conversions/unifications:
    * Units (metric vs. imperial)
    * Numbers (decimals vs. integers)
    * Names (John Smith vs. Smith, John)
    * Time/dates (UNIX vs. UTC vs. GMT)
    * Currency (type, inflation-adjusted, dividends)
    
### Data Imputation

Data imputation is the process of dealing with missing values. The proper methods depend on the type of data we are working with. Gereral methods include:
    * Drop all records containing missing data.
    * Heuristic-based: make a reasonable guess based on knowledge of the underlying domain.
    * Mean Value: fill in missing data with the mean.
    * Random Value
    * Nearest Neighbor: fill in missing data using similar data points.
    * Interpolation: use a method like linear regression to prodict the value of the missing data.
    
### Outlier Detection

Outliers can interfere with analysis and often arise from mistakes during data collection. It makes sense to run a "sanity check".

### Miscellaneous

Lowercasing, removing non-alphanumeric, repairing, unidecode, removing unknown characters.

_Note_: when cleaning data, always maintain both the raw data and the cleaned versions. The raw data should be kept intact and preserved for future use. Any type of data cleaning/analysis should be done on a copy of the raw data.
______________

## Exploratory Data Analysis
[_EDA_](https://en.wikipedia.org/wiki/Exploratory_data_analysis) is an approach, which is promoted by [John Tukey](https://en.wikipedia.org/wiki/John_Tukey), to analyze data sets to summarize their main characteristics, _often with visual methods_. The statistical model can be used or not, but primarily EDA is for seeing what the data can tell us beyond the formal modeling or hypothesis testing task.

### Typical graphical techniques
* Box plot
* Histogram
* Muli-vari chart
* Run chart
* Pareto chart
* Scatter plot
* Stem-Leaf plot
* Parallel coordinates
___________

## Descriptive Statistics
[_Descriptive Statistics_](https://en.wikipedia.org/wiki/Descriptive_statistics) provides a way of capturing a given data set or sample.

There are 3 main types: 
    1. Centrality
    2. Variability (Spread)
    3. Shape
    
### Centrality
* **Arithmetic Mean**: aka _Additive Mean_, it's just simply the average, so it has a severe effect of outliers
* **Geometric Mean**: aka _Multiplicative Mean_. It calculates averaging ratios and the effect of outliers on it is mild. Always less than arithmetic mean.
* **Median**: The median is the midpoint of the ordered dataset or the point that separates dataset in two equal pieces.
* **Mode**: Most frequent element in a dataset.

### Variability
* **Variance** and **Standard Deviation**: Measure the dispersion of a set of data points around its mean value.
    * _Standard Deviation_ == sqrt(_Variance_)
    
* **Coefficient of variation (CV)**: Measure the ratio of dispersion of a single variable or multi-variables with different unit (e.g. usa-vnd).
    * _CV_ == _Standard Deviation_ / _mean_

### Shape
* **Skewness**: Measure the asymmetry that indicates whether the observations in a dataset are concentrated on one side.
    * Positive: the outliers are to the right (long tail to the right in the distribution graph).
    * Negative: the outliers are to the left.

### Correlation Analysis
* **Covariance** and **Correlation**: Measures the joint variability of two variables or the relationship between them. But unlike _covariance_, _correlation_ is standardized measure that takes on values between _(-1 and 1)_.
    * Positive value: 2 variables move together.
    * Negative value: they move in opposite directions.
    * Zero: they are independent.
______

## Inferential Statistics

[Inferential Statistics](https://en.wikipedia.org/wiki/Statistical_inference) is a method that rely on probability theory and **distribution (usually probability distribution)** to predict population values based on sample data.

Two main approaches:
1. **Estimation**: Calculates _Confidence Interval_ to estimate an interval with a certain percentage of confidence the population parameter wil fall.
    
2. **[Hypothesis testing](https://en.wikipedia.org/wiki/Statistical_hypothesis_testing)**: When we are making a decision, we need a yes-no answer. The correct approach in this case is using a test.
    
![Inferential vs. Descriptive -- Population vs. Sample](https://github.com/trungtv4597/Data_project/blob/master/images/Capture.PNG)    
_______

## Feature Engineering
_Feature enginnering (FE)_ is the process of using domain knowledge to create feature or input variables that help machine learning algorithms perform better. Done correctly, it can help increase the predictive power of your models. _FE_ is more of an art than science. It is one of the most important steps in creating a good model. As Andrew Ng puts in:
    _"Coming up with features is difficult, time-consuming, requires expert knowledge. 'Applied machine learning' is basically feature engineering."_
    
### Continuous Data
* **Raw Measures**: data that hasn't been transformed yet.
* **Rounding**: sometimes precision is noise; round to nearest integer, decimal etc..
* **Scaling**: log, z-score, minmax scale, etc...
* **Imputation**: fill in missing values using mean, median, model output, etc...
* **Binning**: trasforming numeric features into categorical ones (or binned) e.g. values between 1-10 belong to A, between 10-20 belong to B, etc...
* **Interactions**: interactions between features: e.g. subtraction, addition, multiplication, statistical test.
* **Statistical**: log/power transorm (helps turn skewed distributions more normal), Box-Cox, etc...
* **Row Statistics**: number of NaN's, 0's, negative values, max, min, etc...
* **Dimensionality Reduction**: using PCA, clustering, factor analysis, etc...

### Discrete Data
* **Encoding**: since some ML algorithms connot work on categorical data, we nee to turn cateforical data into numerical data or vectors.
* **Ordinal Values**: convert each distinct feature into a random number, e.g. (a,b,c) becomes (1,2,3).
* **One-hot Encoding**: each of the m features becomes a vector of length m with containing only one 1, e.g. (a,b,c) becomes ((1,0,0),(0,1,0),(0,0,1)).
* **Feature Hashing Scheme**: turns arbitrary features into indices in a vector or matrix.
* **Embeddings**: if using words, convert words to vectors (word embeddings).
_________

## Modeling - Overview
Modeling is the process of incorporating information into a tool which can forecast and make predictions. Usually, we are dealing with statistical modeling where we want to analyze relationships between variables. Formally, we want to estimate a function **Y = _f(X)_ + re**:
    * X = (X1, X2,..., Xn): The input variables.
    * Y: The output variable.
    * re: random error.
    
**Statistical Learning** is set of appraches for estimating this _f(X)_.    

### Why Estimate _f(X)_?

* **Prediction**: once we have a good estimate _f^(X)_, we can use it to make predictions on new data. We treat _f^_ as a _black box_, since we only care about the accuracy of the predictions, not why or how it works.

* **Inference**: we want to understand the relationship between X and Y. We can no longer treat _f^_ as a black box since we want to understand how Y changes with respect to X.

### More About Random Error
The error term _re_ is composed of the _reducible_ and _irreducible_ error, which will prevent us from ever obtaining a perfect _f^_ estimate.
* **Reducible**: error that can potentially be reduced by using the most appropriate _statistical learning_ technique to estimate _f_. The goal is to minimize the reducible error.
    
* **Irreducible**: error that cannot be reduced no matter how well we estimate _f_. Irreducible error is unknown and unmeasurable and will always be an upper bound for _re_.
    
_Note_: There will always be trade-offs between model flexibility (prediction) and model interpretability (inference). This is just another case of the bias-variance trade-off. Typically, as flexibility increases, interpretability decreases. _Much of statistical learning/modeling is finding a way to balance the two_.    
_________

## Modeling - Philosophies
Modeling is the process of incorporating information into a tool which can forecast and make predictions. Designing and validating models is important, as well as evaluating the performance of models. _Note that the best forecating model may not be the most accurate one_.

### Philosophies of Modeling
* **Occam's Razor**: Philosophical principle that _the simplest explanation is the best explanation_. In modeling, if we are given two models that predicts equally well, we should choose the simpler one. Choosing the more complex one can often result in overfitting.

* **Bias Variance Trade-Off**: To select a best model (for your dataset), _we have to achieve level of complexity that is the trade-off spot between bias and  variance_
    
    * **Bias**: error from incorrect assumptions. _High bias -> missing relevant relations or **underfitting**_
    * **Variance**: error from sensitivity or noise in dataset. _High variance -> modeling noise or **overfitting**_
    
* **No Free Lunch Theorem**: No single machine learning algorithm is better than all the others on all problems. It is common to try multiple models and find one that works best for a particular problem.

### Thinking Like Nate Silver
1. **Think Probabilistically**: Probabilistic forecasts are more meaningful than concrete statements and should be reported as proability distributions (including _var_ along with _mean_ prediction).

2. **Incorporate New Information**: Use live models, which continually updates using new information. To update, use Bayesian reasoning to calculate how probabilities change in respnse to new evidence.

3. **Look For Consensus Forecast**: Use multiple distinct sources of evidence. Some models operate this way, such as boosting and bagging, which uses large number of weak classifiers to produce a strong one.
________

## Modeling - Taxonomy
There are many different types of models. It is important to understand the trade-offs and when to use a certain typer of model.

### Supervised vs. Unsupervised
* **Supervised**: models that fit input variables _x = (x1,...,xn)_ to a known output variables _y = (y1,...,yn)_.

* **Unsupervised**: models that take in input variables _x_, but they don't have an associated output to supervise the training. The goal is understand relationships between the variables or observations.

### Parametric vs. Nonparametric
* **Parametric**: models that first make an assumption about a function form, or shape, or _f_ (e.g. linear). Then fits the model. This reduces estimating _f_ to just estimating set of parameters, but if our assumption was  wrong, will lead to bad results.

* **Non-Parametric**: models that don't make any assumptions about _f_, which allows them to fit a wider range of shapes; but may lead to overfitting.

### Blackbox vs. Descriptive
* **Backbox**: models that make dexisions, but we do not know what happens "under the hood" e.g. deep learning, neural networks.

* **Descriptive**: models that provide insight into why they make their decisions e.g. linear regression, decision trees.

### First-Principle vs. Data-Driven
* **First-Principle**: models based on a prior belief of how the system under investigation works, incorporates domain knowledge (ad-hoc).

* **Data-Driven**: models based on observed correlations between input and output variables.

### Deterministic vs. Stochastic
* **Deterministic**: models that produce a single "prediction" e.g. yes or no, true or false.

* **Stochastic**: models thats produce probability distributions over possible events.

### Flat vs. Hierarchical
* **Flat**: models that solve problems on a single level, no notion of subproblems.

* **Hierarchical**: models that solve several different nested subproblems.
________

## Modeling - Evaluation Metrics
Need to determine how good our model is. Best way to assess models is out-of-sample predictions (data points your model has never seen)

### Classification

![](https://github.com/trungtv4597/Data_project/blob/master/images/classification_index.PNG)

* **Accuracy**: ratio of correct predictions over total predictions. Misleading when class sizes are substantially different. **_accuracy_ = (TP + TN) / (TP+TN+FN+FP)**.

* **Precision**: how often the classifier is correct when it predicts positive. **_precision_ == TP / (TP+FP)**

* **Recall**: how often the classifier is correct for all positive instances. **_recall_ = TP / (TP+FN)**

* **F-Score**: single measurement to describe performance. **_F_ = (2*_precision_*_recall_) / (_precision_*_recall_) **

* **ROC Curves**: plots TP rates and FP rates for various thresholds, or where the model determines if a data point is positive or negative (e.g. if > .8, classify as positive). Best possible area under the ROC curve (AUC) is 1, while random is .5, or the main diagonal line.

### Regression
Errors are defined as the difference between a prediction _y^_ and the actual result _y_.

* **Absolute Error** = |y^ - y|

* **Squared Error** = (y^ - y)^2, more common than _absolute error_ because it's useful for optimizing.

* **Mean-squared Error (MSE)** = sigma(i:1-n)(y^-i - y-i)^2 / (n)

* **Root MSE** = sqrt(_MSE_)
______

## Modeling - Evaluation Environment
_Evaluation metrics_ provides us with the tools to estimate errors, but what should be the process to obtain the best estimate? Resampling involves repeatedly drawing samples from a training set and refitting a model to each sample, which provides us with additional information compared to fitting the model once, such as obtaining a better estimate for the test error.

### Key Concepts
* **Training data**: data used to fit your models or the set used for learning.

* **Validation data**: data used to tune the parameters of a model.

* **Test data**: data used to evaluate how good your model is. Ideally your model should never touch this data until final testing/ evaluation.

### Cross Validation
Class of methods that estimate test error by holding out a subset of training data from the fitting process.

* **Validataion Set**: split data into training set and validation set. Train model on training set and estimate _test error_ using validation set. e.g 80-20 is the most common split.

* **Leave-One-Out**: split data into training set and validation set, but the validation set consists of _only 1_ observation. Then repeat _n-1_ times until all observations have been used as validation. _Test error_ is the average of these _n_ test error estimates.

* **K-Fold**: randomly divide data into _k_ groups (folds) of approximately equal size. First fold is used as validation and the rest as training. Then repeat _k_ times and find average of the _k_ estimates.

### Bootstrapping
Methods that rely on random sampling with replacement. Bootstrapping helps with quantifying uncertainty associated with a given estimate or model.

### Amplifying Small Data Sets
What can we do if we don't have enough data?
    
* **Create Negative Examples**: e.g. classifying presidential candidates, most people would be unqualified so label most as unqualified.
    
* **Synthetic Data**: create additional data by adding noise to the real data.