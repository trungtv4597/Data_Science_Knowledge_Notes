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

## Main Types of Problems
Two problems arise repeatedly in data science:
1. **Classifications**: Assigning something to a discrete set of possibilites. e.g. spam or non-spam, blood type, ...
2. **Regression**: Predicting a numerical value. e.g. someones's income, next year GDP, stock price, ...

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