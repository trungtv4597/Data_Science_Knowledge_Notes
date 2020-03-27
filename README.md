# Overall of Data Science

from: 
1. [Marverick Lin](http://mavericklin.com)
2. [365 Data Science](https://365datascience.com/)
3. [Machine Learning Co Ban by VuHuuTiep](https://github.com/tiepvupsu/ebookMLCB)

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

## Data Sources/ Fomats
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

## Descriptive Statistics
Provides a way of capturing a given data set or sample.

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
____

## Data Cleaning
_Data Cleaning_ is the process of turning raw data into a clean and analyzable data set. "Garbage in, garbage out". Make sure garbage doesn't get put in.

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