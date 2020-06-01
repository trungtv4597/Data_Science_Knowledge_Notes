# The CRISP Data Mining Process

[The CRISP Data Mining Process]()

1. **Business Understanding**
    * Data Mining Common Tasks
    
2. **Data Understanding**
    1. Extraction
        * Flat Files
        * Database
        * Web Scraping
        
    2. Wrangling
        * Cleaning
    
    3. Assessment
        * Descriptive Statistics
        * Exploratory Data Analysis

3. **Data Preparation**
    1. Cluster Analysis
    
4. **Modeling**
    1. Inferential Statistics
        * Estimation
        * Hypothesis Testing
    2. Predictive Model
        * Regression Analysis
        * Logistic Analysis
        
5. **Evaluation**
    
6. **Deloyment**
    * Vusualization
___________________

# Business Understanding
The Business Understanding stage represents a part of the craft where the analysts' creativity plays a large role. Data science has some things to say, but often the key to great success is a creative problem formulation by some analysts regarding how to cast the business problem as one or more data science problems. 

Typically, the early stages of the endeavor involve designing a solution, that can mean structuring (engineering) the problem such that one or more subproblems involve building models for classification,  regression, probability estimation, and so on.

## From Business Problems to Data Mining Tasks
Each data-driven business decision-making problem is unique, comprising its own combination of goals, desires, constraints, and even personalities. Though, there are sets of common tasks that underlie the business problems, data scientists decompose a business problem into subtasks. The solutions to the subtasks can then be composed to solve the overall problem.

> A critical skill in data science is the ability to decompose a data analytics problem into pieces such that each piece matches a known task for which tools are available. Recognizing familiar problems and their solutions avoids wasting time and resources reinventing the wheel. It also allows people to focus attention on more interesting parts of the process that require human involvement - parts that have not been automated, so human creativity and intelligence must come into play.

1. **Classification** and class probability estimation 

They attempt to predict, for each individual in a population, which of a (small) set of classes this individual belongs to.

An example classification question would be: "Among all the customers of MegaTelCo, which are likely to respond to a given offer?" In this example the two classes could be called _will respond_ and _will not respond_.

For a classification task, a data mining procedure produces a model that given a new individual, determines which class that individual belongs to. A closely related task is scoring or _class probability estimation_. A scoring model applied to an individual produces, instead of a class prediction, a score representing the probability (or some other quantification of likelihood) that an individual belongs to each class. In our customer response scenario, a scoring model would be able to evaluate each individual customer and produce a score of how likely each is to respond to the offer.

2. **Regression** or value estimation

It attempts to estimate or predict, for each individual, the numerical value of some variable for that individual. 

An example regression question would be: "How much will a given customer use the service?"

Regression is related to classification, but the two are different. Informally, classification predicts whether something will happen, whereas regression predicts how much something will happen.

3. **Similarity matching**

It attempts to identify similar individuals based on data known about them. Similarity matching can be used directly to find similar entities.

For example, IBM is interested in finding companies similar to their best business customers, in order to focus their sales force on the best opportunities.

Similarity matching is the basis for one of the most popular methods for making product recommendations (finding people who are similar to you in terms of the products they have liked or have purchased).

4. **Clustering**

It attempts to group individuals in a population together by their similarity, but not driven by any specific purpose. 

Clustering is useful in preliminary domain exploration to see which natural groups exist because these groups in turn may suggest other data mining tasks or approaches.

Clustering is used as input to decision-making processes focusing on questions such as: "What products should we offer or develop?" or "How should our customer sales teams be structured?"

5. **Co-occurrence grouping** (aka frequent itemset mining, association role discovery, and market-basket analysis)

It attempts to find associations between entities based on transactions involving them.

An example _co-occrrence_ question would be: "What items are commonly purchased together?"

While clustering looks at the similarity between objects based on the objects' attributes, co-occurrence grouping considers the similarity of objects based on their appearing together in transactions.

Some recommendation systems also perform a type of affinity grouping by finding, for example, pairs of books that are purchased frequently by the same people, "people who bought X also bought Y".

6. **Profiling** (aka behavior description)

It attempts to characterize the typical behavior of an individual, group, or population.

An example _profiling_ question would be: "What is the typical cell phone usage of this customer segment?"

_Profiling_ is often used to establish behavioral norms for anomaly detection applications such as fraud detection and monitoring for intrusions to computer systems.

7. **Link prediction** 

It attempts to predict connections between data items, usually by suggesting that a link should exist, and possibly also estimating the strength of the link. 

Link prediction is common in social networking systems or recommendation systems: "Since you and Karen share 10 friends, maybe you'd like to be Karen's friend?" 

8. **Data reduction**

It attempts to take a large set of data and replace it with a smaller set of data that contains much of the important information in the larger set. And the smaller dataset may be easier to deal with or to process.

Data reduction usually involves loss of information. What is important is the trade-off for improved insight.

9. **Causal modeling**

It attempts to help us understand what events or actions actually influence others.

Techniques for causal modeling include those involving a substantial investment in data, such as randomized controlled experiments (e.g. A/B tests), as well as sophisticated methods for drawing causal conclusions from observational data. Both experimental and observational methods for causal modeling generally can be viewed as "counterfactual" analysis: they attempt to understand what would be the difference between the situations where the "treatment" event were to happen, and were not to happen.
_________________________

# Data Understanding
If solving the business problem is the goal, the data comprise the available raw material from which the solution will be built. It is important to understand the strengths and limitations of the data because rarely is there an exact match with the problem. Historical data often are collected for purposes unrelated to the current business problem, or for explicit purpose at all.

A critical part of the Data Understanding phase is estimating the costs and benefits of each data source and deiding whether further investment is merited. 

In Data Understanding we need to dig beneath the surface to uncover the structure of the business problem and the data that are available, and then match them to one or more data mining tasks for which we may have substantial science and technology to apply. It is not unusual for a business problem to contain several data mining tasks, often of different types, and combining their solutions will be necessary.

## Data Extraction

### Data Scientist as Explorer
In the twenty-first century, data is being collected at unprecedented rates, and in many cases it's not being collected for a specific purpose. Whether whichever type, dat sets are accumulating everywhere. Whereas for centuries data analysts collected thier own data or were given a data set to work on, for the first time in history many people across many industries _are collecting data first_ and then asking, 

> "What can I do with this?" 

Still others are asking, 

>"Does the data already exist that can solve my problem?"

Like an explorer, a modern data scientist typically must survey the landscape, take careful note or surroundings, wander around a bit, and dive into some unfamiliar territory to see what happens. When they find something interesting, they must examine it, figure out what it can do, learn from it, and be able to apply that knowledge in the future. There's so much data that no one can possibly understand it all, so we treat it as a world unto itself, worthy of exploration.

### Where Data Might Live
There are three basic ways to access data:

1. File system

We can read all these files by using our favorite tool. E.g. Excel, Python, ...

But for larger and more complex data sets, it can take minutes or hours for a language like Python to scan a flat-file containing millions of lines of text. In cases where reading files is too slow, there are alternative data storage systems designed to parse through large amounts of data quickly. These are called _databases_.

_Databases_ are data storage systems that have been optimized to store and retrieve data as efficiently as possible within various contexts.

2. Database 

This is also on a file system, but in order to access the data, we have to use the database's interface, which is a software layer that helps store and extract data. E.g. SQL, NoSQL

3. Unknown system

Application programming interface (API), which is a software layer between the data scientist and that system, will help us get data from different or unknown database systems.

### How to Interact with Data
1. **Flat files**
_Flat files_ are plain-vanilla data sets, the default data format in most cases. We can open a flat-file for viewing in a program typically called a text editor which also very available for every major operating system. There are two main subtypes of the flat file:

* _Plain text_: It is the minimal file format for containing words and only words, no style, no fancy images. Numbers and some special characters are OK too.

* _Delimited_: It is plain text with the stipulation of delimiter. It's useful for data contains numerous entries, because if we line up the delimiters properly, it can render information under a table with rows, columns, and headers.

Because they’re so lean, they provide _no additional functionality other than showing the data_, so for larger data sets, flat files become inefficient.

2. **Markup language** 
A _markup language_ is plain text marked up with tags or specially denoted instructions for how the text should be interpreted. 

* The most popular one is _Hypertext Markup Language (HTML)_ and used widely on the Internet to create web pages. HTML is not typically used to store raw data, but because of its popularity, it's containing a lot of data over the Internet. In fact, that concept of _web scraping_ usually entails writing code that can fetch and read web pages and scraping out the specific pieces of the HTML page that are of interest to the scraper.

* _Extensible Markup Language (XML)_ can look a lot like HTML but is generally more suitable for storing and transmitting documents and data other than web pages.

3. **JSON**
Though not a markup language, _JavaScript Object Notation (JSON)_ is functionally similar, at least when storing or transmitting data. Instead of describing a document, JSON typically describes something more like a data structure, such as a list, map, or dictionary in many popular programming languages.

4. **Relational databases**
A _relational database_ is the most common type of database contains data in tabular type, row and column names, and one data point per row-column pair. But not only storing, they are designed to search or _query_ information, and combine or _join_ tables. The main reason why databases are good at retrieving specific data quickly is the _database indexing_.

The most common relational database language for those tasks is _Structured Query Language (SQL)_.

5. **Non-relational databases**
Even if we don't have tabular data, we might still be able to make use of the efficiency of _data indexing_An entire genre of databases called _NoSQL (Not only SQL)_ allows for database schemas outside the more traditional SQL-style relational databases.

6. **APIs**
An _application programming interface (API)_ in its most common forms is a set of rules for communicating with a piece of software. With respect to data, think of an API as a gateway through which we can make requests and then receive the data. Databases have APIs; they define the language that we must use in order to receive the data we want.

The most popular is _REST API_, it's a term that people use when discussing APIs that are accessible via HTTP - meaning we can usually _access them from a web browser_ - and that responds with information in a familiar format, like JSON.

7. **Common bad formats**
The typical suites of _office software_: word processing programs, spreadsheets, mail clients, we should try to avoid them whenever possible and never more so than when doing data science. There usually isn’t a good way to interact with them unless I’m using the highly specialized programs that were built for them, and these programs typically aren’t capable of the analysis that a data scientist usually needs. A _PDF_ can be a tricky thing as well.

8. **Unusual formats**
There are a ton of various data formats around us that are developed for its own purpose. Sometimes those formats are highly specialized, and extremely hard for us to interact with them.

Here's what we should do when we encounter an unusual format:

* Search online for examples of people doing something similar or there are any _file format converters_ the we can use. And figure our how difficult might it be to adapt these examples to our needs? 

* Decide how badly I want the data. Is it worth the trouble? What are the alternatives?

* If it's worth, I try to generalize from the similar examples we found. Then expand from those by fiddling with parameters and methods, try a few things and see what happens.

#### Deciding Which Format to Use
Sometimes you don’t have a choice. The data comes in a certain format, and you have to deal with it. But if you find that format inefficient, unwieldy, or unpopular, you’re usually free to set up a secondary data store that might make things easier, but at the additional cost of the time and effort it takes you to set up the secondary data store.

And here are a few guidelines for choosing or converting data formats:

* For spreadsheets and other office documents, export!

* More common formats are usually better for your data type and application.

* Don’t spend too much time converting from a certain format to your favorite; weigh the costs and benefits first.

As always, never hesitate to ask someone for details about a term or system you haven’t heard of before. New systems are being developed constantly, and in my experience, anyone who recently learned about a system is usually eager to help others learn about it.

### Web Scraping
It's not hard to find data, but finding the data that can help us solve our problem is a different story. Or maybe we already have from an internal system, it may seem like that data can answer the major questions of our project, but we shouldn't take it for granted. Maybe a data set out there will perfectly complement the data we already have and greatly improve results. There's so much data on the Internet; some parts of it should be able to help us. Even if not, a quick search is certainly worth it, even for a long-shot possibility.

#### Scraping vs Crawling

|  Scraping | Crawling  |
|:----------|:----------|
| Involves extracting data from various sources including web | Refers to downloading pages from the web |
| Can be done at any scale | Mostly done at a large scale |
| Deduplication is not necessarily a part | Deduplication is an essential part |
| Needs crawl agent and parser | Needs only crawl agent|

#### Basic Rules

1. The first step is always to look at the raw data. Using _View Page Source_ on web browsers or looking at HTML in a text editor.

2. Reading the HTML line by line and look for the page that contains what we are interested in.

3. Parsing through raw data and extracting the parts that are needed by writing a script in our favorite software. But sometimes, we should consider _Ctrl-C & V_ technique, it might not be the best plan for every project, but it's certainly good in some scenarios.

4. Doble-check everything, because there are no guarantees that we'll arrive at the end of the file in the expected state, maybe scraping people's names in the place of cities and dates in the place of countries.

It fits nicely with a current usage of the word _hacking_ to mean trying a bunch of things until you find a few that get the job done. Being able to load, manipulate, write, and transform data quickly is the most important capability we should strive for when choosing your scripting languages or tools.

#### Demo by Selenium

```python
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# Open your browser
driver = webdriver.Chrome() 
# Access to the target website
url = "https://something.com"
driver.get(url)
# If that website require users to login
username = driver.find_element_by_name('username_element')
password = driver.find_element_by_name('password_element')
username.send_keys('your_username')
password.send_keys('your_password')
driver.find_element_by_class_name('submit_button').click() # command browser to press submit button
# View 50 products each page
select = Select(driver.find_element_by_name('pageSize'))
select.select_by_value(str(50))
# Scrape data
_list = []
xpath_data = '/html/body/div[3]/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/table/tbody'
xpath_pages = '/html/body/div[3]/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[3]/td[2]/table/tbody/tr[1]/td[2]/a[{}]'
i = 1
while True:
    # Access to product page
    try:
        driver.get(driver.find_element_by_xpath(xpath_pages.format(i)).get_attribute('href'))
        list_ = driver.find_element_by_xpath(xpath_data).text
        _list.append(list_)
        i += 1  
    except:
        pass
```

## Data Wrangling

Sometimes, or usually, the way the data is stored in files or databases is not the way we need it for a data processing application. So much of the programming work in data analysis and modeling is spent on _data wrangling_. It is a collection of strategies and techniques:

* Data Cleaning,
* Hierarchical Indexing,
* Combining and Merging Data Sets,
* Reshaping and Pivoting,
* Data Transformation,
* String Manipulation,

that can be applied to take data and information in difficult, unstructured, or otherwise arbitrary formats and converting it into something that meaningful for analysis.

### Data Cleaning
[_Data Cleaning_](https://en.wikipedia.org/wiki/Data_cleansing) is the process of turning raw data into a clean and analyzable data set. "Garbage in, garbage out". Make sure garbage doesn't get put in.

1. Data Compatibility

Data compatibility problems arise when merging datasets. Make sure you are comparing "apples to apples" and not "apples to oranges". Main types of conversions/unifications:
    
* Units (metric vs. imperial)
* Numbers (decimals vs. integers)
* Names (John Smith vs. Smith, John)
* Time/dates (UNIX vs. UTC vs. GMT)
* Currency (type, inflation-adjusted, dividends)

2. Data Imputation

_Data imputation is the process of dealing with missing values_. The proper methods depend on the type of data we are working with. General methods include:

* Drop all records containing missing data.
* Heuristic-based: make a reasonable guess based on knowledge of the underlying domain.
* Mean Value: fill in missing data with the mean.
* Random Value
* Nearest Neighbor: fill in missing data using similar data points.
* Interpolation: use a method like linear regression to predict the value of the missing data.

### Hierarchical Indexing

_Hierarchical indexing_ enables us to have multiple (two or more) index levels on an axis. Somewhat abstractly, it provides a way for us to work with higher dimensional data in a lower-dimensional form.

* At times we will need to rearrange the order or **reorder** of the levels on an axis and **sort** the data by the values at one specific level.

* **Using columns as indexes**

```python
df.set_index(['name_of_columns'])
```

### Combining and Merging Data Sets

If we find that our data set is insufficient to answer your questions, and we can't find one that is sufficient, it might still be possible to combine data sets to find ansers.

* **Merging**: connects rows based on one or more keys, overlapped columns or index.

```python
pandas.merge(df1, df2, left_key, right_key)
```

* **Concatenating**: glues or stacks together objects along an axis.

```python
pandas.concat([df1, df2], axis)
# axis: 0-indexs, 1-columns
```

* **Combining for update null elements**: splices together overlapped data to fill in missing values in one object with values from another.

```python
df1.combine_first(df2)
# Update null elements in the df1 with value in the same location in df2.
```

### Reshaping and Pivoting
These are a number of fundamental operations for rearranging tabular data. These data alternatingly referred to as _reshape_ or _pivot_ operations.

* **Stacking**: rotates from the columns in the data to the rows.

* **Unstacking**: rotates from the rows into the columns.

* **Pivoting "stacked" to "unstacked" format**: creates a _hierarchical index_ and then _unstack_ it. For example, time-series data is commonly stored in databases with _stacked format_. It's quite hard to work with this format, so we might prefer to have a table containing one column per distinct value and indexed by timestamps. The _pivot_ method helps us that.

```python
time_series_df.pivot(index, columns, values)
```

### Data Transformation
* **Remove duplicates**

* **Transform data using a function or mapping**: for many data sets, we may wish to perform some transformation based on the values in an array, list, dictionary, table,...

* **Replace values**

* **Rename indexes & columnes**
```python
df.rename(index={'original_name':'replace_name'},
          columns={'original_name':'replace_name'})
```

* **Binning**: Continuous data should be separated or _pandas.cut_ into _bins_ for analysis.

* **Detect outliers**

* **Permutation and random sampling**
```python
sampler = numpy.random.permutations(length_of_the_axis)
df.take(sampler)
```

* **Compute dummy**: transformation for statistical modeling or machine learning applications is converting a categorical variable into _dummy_ or _indicator_ matrix.

### String Manipulation
* **String object methods**: _contains_ , _split_ , _join_ , _index_ , _count_ , _replace_ , _find with patters_ , ...

* **Regular expressions**: provide a flexible way to search or match string patterns in text.

_Note_: when cleaning data, always maintain both the raw data and the cleaned versions. The raw data should be kept intact and preserved for future use. Any type of data cleaning/analysis should be done on a copy of the raw data.

## Descriptive Statistics
A definition from [Wikipedia](https://en.wikipedia.org/wiki/Descriptive_statistics):

> Descriptive statistics provide simple summaries about the sample and about the observations that have been made. Such summaries may be either quantitative, i.e. summary statistics, or visual, i.e. exploratory data analysis. 

It's often hard to discuss descriptive statistics without mentioning inferential statistics. Inferential statistics is the practice os using the data we have to deduce - or infer - knowledge or quantities of which we don't have direct measurements or data. With respect to a data set, we can say the following:

* Descriptive statistics asks, _"What do I have?"_

* Inferential statistics asks, _"What can I conclude?"_

Descriptive statistics are distinguished from inferential statistics by its aim to summarize a sample, rather than use the data to learn about the population that the sample of data is thought to represent.

Although descriptive and inferential statistics can be spoken of as two different techniques, the border between them is often blurry. In common sense, we would have to perform descriptive stat on the sample set in order to infer anything about the population, but it isn't always clear where the description stops and where the inference starts.

### Why Do We Need It?
The purpose of calculating descriptive statistics at this stage in a data science project is to learn about your data set so that you understand its capabilities and limitations; trying to do anything but learn about our data at this point would be a mistake. 

Complex statistical techniques such as those in machine learning, predictive analytics, and probabilistic modeling, for example, are completely out of the question for the moment. Complex methods like most of those used in machine learning today are not easily dissected or even understood. Random forests, neural networks, and among others, may be understood in theory, but each of these has so many moving parts that one person (or a team) can't possibly comprehend all of the specific pieces and values involved in obtaining a single result. Therefore, when we notice an incorrect result, even one that's grossly incorrect, it's not straightforward to extract from a complex model exactly which pieces contributed to this egregious error. More importantly, complex models that involve some randomness may not reproduce a specific error if you rerun the algorithm. It's always the better choice for us to stay close to our own data first before we allow any random processes or black boxes to draw conclusions for us.

In addition, there are always issues while wrangling the data, but it may have slipped past unnoticed, and some descriptive statistics can help us catch it now. 

One way to realize if we are still close to the data:

> We are close to the data if we are computing statistics that we are able to verify manually or that we can replicate exactly using another statistical tool.

Staying close to the data ensures that we can be incredibly certain about these preliminary results, and keeping a set of good descriptive statistics with you throughout our project provides us an easy reference to compare with subsequent more relevant but more abstruse results that are the real focus of your project.

### Summary Statistics
A definition from [Wikipedia](https://en.wikipedia.org/wiki/Summary_statistics):

> Summary statistics are used to summarize a set of observations, in order to communicate the largest amount of information as simply as possible. There are 4 aspects to describe our data or more explicitly the distribution of our data.  

* Univariate
    1. Centrality
    2. Variability (Spread)
    3. Shape
* Multivariate
    4. Dependency

#### Centrality
* **Arithmetic Mean**: aka _Additive Mean_, it's just simply the average, so it has a severe effect of outliers
* **Geometric Mean**: aka _Multiplicative Mean_. It calculates averaging ratios and the effect of outliers on it is mild. Always less than the arithmetic mean.
* **Median**: The median is the midpoint of the ordered dataset or the point that separates the dataset in two equal pieces.
* **Mode**: Most frequent elements in a dataset.
* **Interquartile Mean**: is very similar to the scoring method used in sports that are evaluated by a panel of judges: _discard the lowest and the highest scores; calculate the mean value of the remaining scores_.

#### Variability
* **Variance** and **Standard Deviation**: Measure of the dispersion of a set of data points around its mean value.
    * _Standard Deviation_ == sqrt(_Variance_)
    * 1 std of a distribution contains 68% of all data points.
    
* **Interquartile Range (IQR)**: computes sample quantile. The most common is the _five-number summary_ - min/25th/50th/75th/max.    
    
#### Shape
* **Skewness**: Measure the asymmetry that indicates whether the observations in a dataset are concentrated on one side.
    * _Positive_ : the outliers are to the right (long tail to the right in the distribution graph).
    * _Negative_ : the outliers are to the left
    
* **Kurtosis**: muốn nói đến hình dạng của phân phối theo chiều cao hoặc theo độ phẳng.
    * _Leptokurtic_: nhọn lép, khi một phân phôi có đỉnh cao hơn so với đỉnh ở một phân phối chuẩn. Một phân phối nhọn lép có thể có tỷ lệ phần trăm các điểm gần trung bình cao hơn còn các điểm xa trung bình.
    * _Platykurtic_: nhọn đầy, khi một phân phối phẳng hơn so với phân phối chuẩn. Một  phân phối nhọn đầy sẽ có nhiều điểm ở hai đầu hơn và ít điểm ở vùng giữa hơn so với phân phố chuẩn.
    
#### Dependency
* **Coefficient of variation (CV)**: Measure of the ratio of dispersion of a single variable or multi-variable with different units (e.g. usa-vnd).
    * _CV_ == _Standard Deviation_ / _mean_
    
* **Covariance**: Measure of the joint variability of two variables.
    * _Positive_ : The two variables move together.
    * _Negative_ : They move in opposite directions.
    * _0 (zero)_ : They are independent.
    
* **Correlation**: Because _covariance_ can take on values from negative to positive-infinity, this is hard to intuitively interpret. _Correlation_ is a standardized measure of the joint variability of two variables. It only takes on values _between -1 and 1_.
    
    * _1_ : That means one variable is perfectly explained by the other.
    * _(-1)_ : This is also explaining the other one perfectly, but they move in opposite directions.
    * _0_: They are independent variables.


## Exploratory Data Analysis
_Tables and graphs_ can convey information more thoroughly and more quickly at times than pure text. Producing tables and graphs and keeping them for reference throughout your project is a good idea.

[_EDA_](https://en.wikipedia.org/wiki/Exploratory_data_analysis) is an approach, which is promoted by [John Tukey](https://en.wikipedia.org/wiki/John_Tukey): 

> To analyze data sets to summarize their main characteristics, _often with visual methods_. The statistical model can be used or not, but primarily EDA is for seeing what the data can tell us beyond the formal modeling or hypothesis testing task.

### Types of data
1. **Categorical**: FC (Man Utd, Barca, Real,..), Yes-No question, ...

2. **Numerical**

    * **Discrete**: SAT score, number of chidren we have,... 
    * **Continuous**: weight, height,...
    
### Graphs and Tables for Categorical
* **Frequency distribution tables**: Show the category and its corresponding absolute frequency.

* **Bar charts**: Each bar represents a category and on the y-axis we have the absolute frequency.

```python
import seaborn as sns
sns.catplot(data, x, y, hue, kind='bar')
```

* **Pie charts**: Show the share of an item as a part of the total or relative frequency.

```python
import pandas as pd
series.plot(kind='pie', autopct='%1.1f%%')
```

* **Boxplot**: This kind of plot shows the three quartile values of the distribution along with extreme values. The “whiskers” extend to points that lie within 1.5 IQRs of the lower and upper quartile, and then observations that fall outside this range are displayed independently.

```python
import seaborn as sns
sns.catplot(data, x, y, hue, kind='box')
```

* **Pareto diagrams**: Represent 80/20 rule, the categories are shown in descending order of frequency, and a separate curve shows the cumulative frequency

### Graphs and Tables for Numerical
* **Frequency distribution tables**: These ones for numberical variables are different than the ones for categorical. The tables are divided into intervals of equal length and show the absolute frequency of each interval. Interval witdth = (max - min) / number of desireed intervals.

* **Histogram**: Like bar charts, but for representing intervals. A histogram represents the distribution of data by forming bins along the range of the data and then drawing bars to show the number of observations that fall in each bin.

```python
import seaborn as sns
sns.distplot(data, kde=False, rug=True)
```

* **KDE plots**: The kernel density estimate may be less familiar, but it can be a useful tool for plotting the shape of a distribution. Like the histogram, the KDE plots encode the density of observations on one axis with height along the other axis.

```python
import seaborn as sns
sns.distplot(data, hist=False, rug=True)
```

### Graphs and Table for Relationships
1. Categorical
    
    * **Pivot tables**: This table is a data summarization tool which aggregates a table of data by one or more keys, arranging the data with some of the group keys along the rows and sone along the columns. We can fill in the table with the applicable data
    
    * **Cross-tabulation**: This is a special case of a pivot table that computes group relative frequencies.
    
    * **Side-by-side bar charts**: For visualizing pivot-tables and cross-tabulation.
    
2. Numerical
    
    * **Scatter plots**: Are useful for regression analysis, as the help us detect patterns (linearity, homoscedasticity).

    ```python
    import seaborn as sns
    
    # standard plot
    sns.relplot(data, x, y, hue)
    
    # bivariate distribution
    sns.jointplot(data, x, y) 
    
    # multivariate
    sns.pairplot(data)
    
    # regression with a single relationship
    sns.regplot(data, x, y)
    
    # regression with more complex level
    sns.lmplot(data, x, y, hue, col, order=degree_equation)
    ```

    * **Line plots**: With some datasets, you may want to understand changes in one variable as a function of time, or a similarly continuous variable. In this situation, a good choice is to draw a line plot
    
    ```python
    import seaborn as sns
    sns.relplot(data, x, y, kind='line')
    ```
    
## Assessment Examples

1. **Summary statistics table** 

    * _Count_: learn how many data points are there and determine which feature is containing null value (have fewer count value than others).

    * Categorical: _Unique_ / _Mode_ / _Frequency_ / _Cumulative_.

    * Numerical: _Mean_ / _std_ / _Percentiles_ / _Min-Max_ / _Sum_.

```python
def summary_statistics(df, stats):
    d = df.describe(include='number', percentiles=[.25, .5, .75, .90]) # standard describe tables
    d_plus = df[d.columns].agg(stats) # more statistics methods
    return pd.concat([d, d_plus]) # concatenation

summary_statistics(df, ['sum'])
```

2. **Bucket analysis table**

```python
import numpy as np
import pandas as pd

def get_stats(group):
    return {'count': group.count(),
            'sum': group.sum(),
            'mean': group.mean(),
            'median': group.median(),
            'max': group.max(),
            'min': group.min()}

bins = np.array([]) # Your customer interval
factor = pd.cut(series, bins)
grouped = series.groupby(factor)
grouped.apply(get_stats).unstack()
```
3. **Dual Comparison**

```python
def get_top_score(group, key, n=5):
    totals = group.groupby(key)['score'].sum()
    return totals.order(ascending=False)[-n:]
    
grouped = data.groupby(data['candidates'])
grouped.apply(get_top_score, 'field')
```

4. **Pivot-table**

```python
df.pivot_table(values='score',
               rows='candidates',
               cols='field')

```

5. **Pareto chart**

```python
import numpy as np
import pandas as pd
df.sort_values(by='frequency', inplace=True)
df['cumulative_frequency'] = df['frequency'].cumsum()

from matplotlib import pyplot as plt
from matplotlib.ticker import PercentFormatter
fig, ax1 = plt.subplots(figsize=())
ax1.bar(x=df.index, height=df['frequency'])

ax2 = ax1.twinx()
ax2.plot(x=df.index, y=df['cumulative_frequency'], marker='D')
ax2.yaxis.set_major_formatter(PercentFormatter())
```


# Data Prepation

# Modeling
The Modeling stage is the primary place where data mining techniques are applied to the data.

# Evaluation
The purpose of the evaluation stage is to assess the data mining results rigorously and to gain confidence that they are valid and reliable before moving on.

Equally important, the evaluation stage also serves to help  ensure that the model satisfies the original business goals. Recall that the primary goal of data science for business is to support decision making, and that we started the process by focusing on the business problem we would like to solve.

# Deployment
The clearst cases of deployment involve implementing a predictive model in some information system or business process.

In many cases, the data science team is responsible for producing a working prototype, along with its evaluation. These are passed to a development team. It may be helpful to remember the maxim: "Your model is not what the data scientists design, it's what the engineers build."

Regarless of whether deployment is successful, the process often returns to the Business Understanding phase. The process of mining data produces a great deal of insight into the business problem and the difficulties of its solution. A second iteration can yield an improved solution.