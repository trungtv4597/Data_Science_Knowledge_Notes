# Overall of Probability and Statistics
---

## Linear Algebra

* Linear algebra is the branch of mathematics that deals with _vector spaces_.

* It underpins a large number of data science concepts and techniques.

### Vector

* The simplest from-scratch approach is to represent vectors as lists of numbers.

* Vectors are objects that can be added together (to form new vectors) and that can be multiplied by _scalars_ (i.e., numbers) also to form new vectors.

* _The dot product_ measures how far the vector **v** extends in the the **w** direction. Another way of saying this is that it's the **length** of the vector you'd if you projected **v** onto **w**.

### Matrices

* A _matrix_ is a 2-d collection of numbers, so we can represent matrices as _lists of list_.

* Matrices wil be important to us for several reasons:

1. We can use a matrix to represent a data set consisting of multiiple vectors, simply by considering each vector as a row of the matrix.

2. Matrices can be used to represent binary relationships.
---

## Statistics
* _Statistics_ refers to the mathematics and techniques with which we understand data.

### Describing a Single Set of Data

#### Central Tendencies
Usually, we'll want some notion of where our data is centerd.

1. **mean**: is simply the point halfway between 2 data points. As you add more points, the mean shifts around, but it always _depends on the value of every point_.

2. **median**: is the _middle-most_ value. For instance, if we have 5 data points in a stored vector x, the median is x[5 // 2] or x[2], if we have 6 data points, it's gonna be the average of x[2] and x[3]. 

* Note: the _mean_ focus on *values*, the _median_ focus on *position* and doesn't depend on every value in your data. So if you make largest point larger the middle points remain unchanged. The mean is very sensitive to outliers in our data. For example, the story is often told that in the mid-80s, the major at the University of North caolina with the highest average starting salary was _geography_ mostly on accounts of NBA star (and outlier) Michael Jordan.

3. **mode**: is the _most-common_ value.

4. **quantile**: represents the value less than which a certain percentile of the data lies. For instance, _median_ is the _middle-most_ value of whole data set, _quantile_ is the _median_ in higher and lower set. _quantile_ seperates our data into 4 equally set.

#### Dispersion
_Dispersion_ refers to measures of how spread out our data is.

1. **range**: is just the difference between the largest and smallest elements. Like the median, the _range_ doesn't really depend on the whole data set.

2. **variance**: is average of squares the far of all data points from its mean. var = Sigma(i, n)[(X[i] - x_bar)/(n-1)]. 
* Note: dividing by _n-1_ instead of _n_ beacause we're dealing with a sample from a larger poplation, _xbar_ is only an estimate of the actual mean.

3. **standard_deiation**:  _variance_ has units that are the _square_ of the orighinal units, so we need the the normal unit. _std = sqrt(variance)_.

### Comparing Several Sets of Data

#### Correlation

1. **covariace**: whereas _variace_ measures how single variable deviates from its mean, _covariace_ measures how two variables vary in tandem from their means. When corresponding elements of _x_ and _y_ are either both above or below their means or, it'll a _positive number_. When one is above and the other below, it'll a _negative number_.

2. _covariace_ is hard to interpret, it's more common to look at the **correlation**: is unitless and always lies between _-1 (perfect anti-correlation) and 1 (perfect correlation). However _correlation_ can be very sensitive to outliers. So we can robust correlation by ignoring outliers.

* Note: The sort of relationship the _correlation_ looks for is in which knowing how x_i compares to mean(x) give information about how y_i compares to mean(y).

#### Correlation and Causation
* "Correlation might not be causation". if x and y are strongly correlated, that might mean that _x causes y_, that _y causes x_ that _each causes the other_, that _some third factor caused both_, or _it might mean nothing_.

* One way to feel more confident about causality is by _conducting randomized trials_. If you can randomly split your users into two groups with similar demographics and give one of the groups a slightly different experience, the you can often feel pretty good that the different experiences are causing the differenct outcomes.
---

## Probability
**P(E)** means "the probability of the event E".

### Dependence and Independence
* We can say that 2 events X and Y are _dependent_ if knowing something about whether A happens gives us information about whether B happens. Otherwise they are _independent_.

* A and B are _independent_: the probability that they both happen is the product of the probabilities that each on happen. *P(A, B) = P(A)P(B)*

#### Conditional Probability
* A and B are _dependent_: the probability of A happens, given that we know that B happens ("conditional on B"). *P(A |B) = P(A, B)/P(B)*

#### For example: a family with two (unknown) children
1. Each child is eqally likely to be a boy or a girl.

* P(b) = 1/2
* P(g) = 1/2

##### => P(both_b) = P(both_g) = 1/2 * 1/2 = 1/4

2. The gender of the second child is independent of the gender of the first child. 
##### => P(b, g) = P(g, b) = 1/4

3. The order doesn't matter.
##### => P = 2 * 1/4 = 1/2

4. The gender of _the older child is a girl_
##### => P(both_g |g) = P(both_g)/P(g) = 1/4 * 2 = 1/2

5. Know at least one of them is a girl.

* P(l) = P(both_g) + P(b, g) + P(g, b) = 3/4
##### => P(b |l) = 1/4 * 4/3 = 1/3

### Bayes's Theorem
It is a way of "reversing" conditional probabilities. Let's say we need to know the probability of same event A conditional on some other event B occring. But we only have information about the probability of F conditional on E occurring.

* **P(A |B) = P(B |A)P(A)/P(B)**

with Abar mean "not A" => P(B) = P(B, A) + P(B, Abar)

* **P(A |B) = P(A |B)P(A) / [P(B |A)P(A) + P(B | Abar)P(Abar)]**

### Random Variables

* It is a variable whose possible values have an associated probability distribution.

* Going back to the 2-child example. If X is the random variable representing the number of girls. P(X = 0) = 1/4, P(X = 1) = 1/2, P(X = 2) = 1/4. We can define Y that gives conditional on at least one girl P(X = 2 |Y) = 1/3.

### Continuous Distributions

* A coin flip corresponds to a _discrete distribution_-one that associates positive probability with _discrete outcomes_.

* But how about price prediction, there are infinitely many numbers between numbers. This is a _continuous distribution_, and we can represent it with **probability density function (pdf)**  such that probability of seeing a value in a certain interval equals the intergral of the density function aver the interval. Or simpler way of understanding if a distribution has density function (_f_), then the probability of seeing a value betwen _x_ and _x_ + _h_ is approximately _h* f(x).

* **cumulative distribution function (cdf)** gives the probability that a random variable is less than or equal to a certain value.

### The Normal Distribution

* The normal distribution is the king of distribution:
1. It approximates a wide variety of random vaiables.
2. Distributions of sample means with large enough samples sizes could be approximated to normal.
3. All computatble statistics are elegant.
4. Heavily used in regression analysis.
5. Good track record.
6. Applying _central linmit theorem_

* It is completely determined by two parameters: its _mean (mu)_ and its _standard deviation (sigma)_.

* When _mu_ = 0 and _sigma_ = 1, it's called the _standard normal distribution_. if _Z_ is a standard normal random variable: **Z = (X - _mu_)/_sigma_**

### The Central Limit Theorem

* The CLT is one of the greatest statistical insights. It states that no matter the underlying distribution of the dataset, the sampling distribution of the means would approximate a normal distribution.
1. The mean of the sampling distribution would be equal to the mean of the original distribution.
2. The variance would be **n** times smaller, where **n** is the the size of samples.

* The CLT applies whenever we have a sum or an average of many variables.
