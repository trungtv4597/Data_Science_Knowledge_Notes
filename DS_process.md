
# The Lifecycle of a Data Science Project

[From: Think Like a Data Scientist by Brian Godsey](https://www.manning.com/books/think-like-a-data-scientist)

A data science project is organized around the _three phases_ or _12 steps_:
* **Preparation**: gathering information at the beginning.
    
1. [_Set Goals_](#goals)
2. [_Extract_](#extraction)
3. [_Wrangle_](#wrangling)
4. [_Assess_](#assessment)

* **Building**: from planning through execution, using what you learned during the **preparation** and all the tools that statistics and software can provide to build the product.    

5. [_Plan_]()
6. _Analyze_
7. _Engineer_
8. _Optimize_
9. _Execute_

* **Finishing**: delivering the product, getting feedback, making revisions, supporting the product, and wrapping up the project.
    
10. _Deliver_
11. _Revise_
12. _Wrap up_

______________________________

<div id='goals'/>

# Setting Goals 

In a data science project, as in many other fields, the main goals should be set at the beginning of the project. All the work you do after setting goals is making use of data, statistics, and programming to move toward and achieve those goals.

There are two situations we usually start off a data science project:

1. **Customer come to us with a _expectation_**: No matter who the customer might be, they have some expectations about what they might receive from you as a data scientist. Often these expectations relate to the following:

    * Questions that need to be answered or problems that need to be solved.
    
    * A tangible final product, such as a report or software application.
    
    * Summaries of prior research or related projects and products.

2. **Customer come to us with a _dataset_**: They hope you can explore it as much as possible the valuable information.

## Deal with Expectations
A typical discussion of expectation boils down to two sides: 

* What the customer wants.

* what the data scientist thinks is possible. 

This could be described as **wishes vs. pragmatism**, with the customer describing thier desires and the data scientist approving, rejecting, or qualifying each one based on apparent feasibility.

**In this situation, a project in data science begins by _finding agreement between the customer and the data scientist_.**

Some methods to figure out that agreement:

* Asking specific question that give us some **intuitive sense** how the system under investigation works.

* Uncovering **fact, not opinions**: When a customer is describing a theory or hypothesis about the system that we're about to investigate, they are almost certainly expressing a mixture of fact and opinion. So in their answer, it is very important to distinguish between what they think and what they know.

* Suggesting deliverables: Asking them "What would you like to appear in the final report?" or "What should this analytic application do?" can easily result in "I don't know" or, even worse, a suggestion that doesn't make sense. It's usually best approach the question of final product with a series of syggestions and then to note the customer's reaction, like _"Can you give me an example of a sentence that you might like to see in a final report?"_.

* **Don't confuse of correlation and causation**: For example, the correlation between helmets and accidents doesn't imply that helmets cause accidents; nor does it imply that accidents cause the wearing of helmets (directly). So there's no direct causation despite the existence of correlation.

## Deal with Datasets
These are the two most dangerous pitfalls:

* Expecting the data to be able to answer a question it can't.

* Asking the question of the data that don't solve the original problem.

**In this situation, setting goals by asking questions that lead to informative answers ans subsequently improved results.**

No question is quite as tricky to answer as one that's based on faulty assumptions and a question based on unclear assumptions is a close second. So a good question require a concrete assumption, or it's well defined and able to be tested. 

One way to acknowledge the assumptions is to _break down all of the reasoning between analysis, argument and conclusion into specific logical steps_ and to make sure that all of the gaps are filled in. For example, think of all of the things _X_ could be anything -stock price, rainfall, ... - the logic should be:

1. X has gone down recently.

2. Because X always corrects itself towards a certain value, V.

3. X will go up soon, toward V.

The data tells us _1_ and _3_ is the conclusion we draw. _2_ is the argument and _3_ is dependent on _2_ being true. So we can easily test this assumption by justifying its argument.

## Planning
### Has Someone Done This Before?
This should always be the first step in developing a plan, check the internet for:

* Blog posts,
* Scientific articles,
* Open-source projects,
* Research descriptions from unversities
* Anything else that relate to the project we're starting.

If someone else has done something similar, you may gain a lot of insighit into the challenges and capabilities that you haven't yet encountered. But _awareness_ is very helpful.

### Is the Data Relevant and Sufficient?
All we are talking about is the **data-centric** project, so data should be considered very carefully.

There is a way to measure how our data is relevant or sufficient, it is to **outline** specifically how data will help us answer our question. For example, the investigation of affinity for beer types, such a statement might suffice:

> In order to find out whether beer drinker like certain types of beers significantly more than others, we need data containing _beer name, beer type, user names and thier ratings_. With this data, we can perform a statistical test, such as ANOVA, with each beer type as a variable, and examine whether beer type is a significant influencer of rating for individual users.

By stating what specific properties the data set should have, we can check quickly to see if the data set fulfills the requirements.

_Note: A good outline states what data we would need and how we would use that data to answer the question. In some ways, we can build a plan from it._

### Be Flexible

* It's always a good strategy to think of a few different ways that you might achieve your goals, even the goals themselves can be flexible.

* There are _uncertainties_ in the project, it's btter to map out all of the most likely paths, each path is very _from the beginning to the first major uncertainty_.

* The plan we formulate here will be revisited periodically throughout the project, so a good plan is to put us in the best position to be well informed the next time we revisit plans and goals.

_________________

<div id='extraction'/>

# Data Extraction

## Data Scientist as Explorer
In the twenty-first century, data is being collected at unprecedented rates, and in many cases it's not being collected for a specific purpose. Whether whichever type, dat sets are accumulating everywhere. Whereas for centuries data analysts collected thier own data or were given a data set to work on, for the first time in history many people across many industries _are collecting data first_ and then asking, 

> "What can I do with this?" 

Still others are asking, 

>"Does the data already exist that can solve my problem?"

Like an explorer, a modern data scientist typically must survey the landscape, take careful note or surroundings, wander around a bit, and dive into some unfamiliar territory to see what happens. When they find something interesting, they must examine it, figure out what it can do, learn from it, and be able to apply that knowledge in the future. There's so much data that no one can possibly understand it all, so we treat it as a world unto itself, worthy of exploration.

## Where Data Might Live
There are three basic ways to access data:

1. File system: We can read all these files by using our favorite tool. E.g. Excel, Python, ...

But for larger and more complexity data sets, it can take minutes or hours for a language like Python to scan a flat file containing millions of lines of text. In cases where reading files is too slow, there are alternative data storage systems designed to parse through large amounts of data quickly. These are called _databases_.

_Databases_ are data storage systems that have been optimized to store and retrieve data as efficiently as possible within various contexts.

2. Database: Which is also on a file system, but in order to acces the data, we have to use database's interface, which is a software layer that helps store and extract data. E.g. SQL, NoSQL

3. Unknown system: Application programming interface (API), which is a software layer between the data scientist and that system, will help us get data.

## How to Interact with Data
1. **Flat files**
_Flat files_ are plain-vanilla data sets, the default data format in most cases. We can open a flat file for viewing in a program typically called a text editor which also very available for every major operating system. There are two main subtypes of the flat file:

* _Plain text_: It is the minimal file format for containing words and only words, no style, no fancy images. Numbers and some special characters are OK too.

* _Delimited_: It is plain text with the stipulation of delimiter. It's useful for data contains numerous entries, because if we line up the delimiters properly, it can render information under a table with rows, columns and headers.

Because they’re so lean, they provide _no additional functionality other than showing the data_, so for larger data sets, flat files become inefficient.

2. **Markup language** 
A _markup language_ is plain text marked up with tags or specially denoted instructions for how the text should be interpreted. 

* The most popular one is _Hypertext Markup Language (HTML)_ and used widely on the Internet to create web pages. HTML is not typically used to store raw data, but because of its popular, it's contaning a lot of data over the Internet. In fact, that concept of _web scraping_ usually entails writing code that can fetch and read web pages and scraping out the specific pieces of HTML page that are of interest to the scraper.

* _Extensible Markup Language (XML)_ can look a lot like HTML but is generally more suitable for storing and transmiiting documents and data other than web pages.

3. **JSON**
Thought not a markup language, _JavaScript Object Notation (JSON)_ is functionally similar, at least when storing or transmitting data. Instead of describing a document, JSON typically describes something more like a data strcture, such as a list, map, or dictionary in many popular programming languages.

4. **Relational databases**
A _relational database_ is the most common type of database contains data in tabular type, row and column names and one data point per row-column pair. But not only storing, they are designed to search or _query_ information, and combine or _join_ tables. The main reason why databases are good at retrieving specific data quickly is the _database indexing_.

The most common relational database language for those task is _Structured Query Language (SQL)_.

5. **Non-relational databases**
Even if we don't have tabular data, we might still be able to mmake use of the efficiency of _data indexing_An entire genre of databases called _NoSQL (Not only SQL)_ allows for database schemas outside the more traditional SQL-style relational databases.

6. **APIs**
An _application programming interface (API)_ in its most common forms is a set of rules for cmmunicating with a piece of software. With respect to data, think of an API as a gateway through which we can mak requests and then receive the data. Databases have APIs; they define the language that we must use in order to receive the data we want.

The most popular is _REST API_, it's a term that people use when discussing APIs that are accessible via HTTP - meaning we can usually _access them from a web browser_ - and that respond with information in a familiar format, like JSON.

7. **Common bad formats**
The typical suites of _office software_: word processing programs, spreadsheets, mail clients, we should try to avoid them whenever possible and never more so than when doing data science. There usually isn’t a good way to interact with them unless I’m using the highly specialized programs that were built for them, and these programs typically aren’t capable of the analysis that a data scientist usually needs. A _PDF_ can be a tricky thing as well.

8. **Unusual formats**
There are a ton of various data formats around us which are developed for its own purpose. Sometimes those formats are highly specialized, and extremely hard to us to interact with them.

Here's what we should do when we encounter a unusual format:

1. Search online for examples of people doing something similar or there are any _file format converters_ the we can use. And figure our how difficult might it be to adapt these exmaples to our needs? 

2. Decide how badly I want the data. Is it worth the trouble? What are the alternatives?

3. If it's worth, I try to generalize from the similar examples we found. Then expand from those by fidding with parameter and methods, try a few things and see what happens.

## Deciding Which Format to Use
Sometimes you don’t have a choice. The data comes in a certain format, and you have to deal with it. But if you find that format inefficient, unwieldy, or unpopular, you’re usually free to set up a secondary data store that might make things easier, but at the additional cost of the time and effort it takes you to set up the secondary data store.

And here are a few guidelines for choosing or converting data formats:

* For spreadsheets and other office documents, export!

* More common formats are usually better for your data type and application.

* Don’t spend too much time converting from a certain format to your favorite; weigh the costs and benefits first.

As always, never hesitate to ask someone for details about a term or system you haven’t heard of before. New systems are being developed constantly, and in my experience, anyone who recently learned about a system is usually eager to help others learn about it.

## Web Scraping
It's not hard to find data, but finding the data that can help us solve our problem is a different story. Or maybe we already have from an internal system, it may seem like that data can answer the major questions of our project, but we shouldn't take it for granted. Maybe a data set out there will perfectly complement the data we already have and greatly improve results. There's so much data on the Internet; some part of it should be able to help us. Even if not, a quick search is certainly worth it, even for a long-shot possibility.

1. The first step is always look at the raw data. Using _View Page Source_ on web browsers or looking at HTML in a text editor.

2. Reading the HTML line by line and look for the tage that contains what we are interest in.

3. Parsing thourgh raw data and extracting the parts that are needed by writting a script in our favourite software. But sometimes, we should consider _Ctrl-C & V_ teachnique, it might not be the best plan for every project, but it's certainly good in some scenarios.

4. Doble-check everything, because there are no guarantees that we'll arrive at the end of the file in the expected state, maybe scraping people's names in the place of cities and dates in the place of countries.

It fits nicely with a crrent usage of the word _hacking_ to mean trying a bunch of things until you find a few that get the job done. Being able to load, manipulate, write, and transform data quickly is the most important capability we should strive for when choosing your scripting languages or tools.

______________

<div id='wrangling'/>

# Data Wrangling

Sometimes, or usually, the way the data is stored in files or database is not the way we need it for a data processing application. So much of the programming work in data analysis and modeling is spent on _data wrangling_. It is a collection of strategies and techniques:

* Data Cleaning,
* Hierarchical Indexing,
* Combining and Merging Data Sets,
* Reshaping and Pivoting,
* Data Transformation,
* String Manipulation,

that can be applied to take data and information in difficult, unstructured, or otherwise arbitrary formats and converting it into something that meaningful for analysis.

## Data Cleaning
[_Data Cleaning_](https://en.wikipedia.org/wiki/Data_cleansing) is the process of turning raw data into a clean and analyzable data set. "Garbage in, garbage out". Make sure garbage doesn't get put in.

### Data Compatibility

Data compatibility problems arise when merging datasets. Make sure you are comparing "apples to apples" and not "apples to aranges". Main types of conversions/unifications:
    
* Units (metric vs. imperial)
* Numbers (decimals vs. integers)
* Names (John Smith vs. Smith, John)
* Time/dates (UNIX vs. UTC vs. GMT)
* Currency (type, inflation-adjusted, dividends)

### Data Imputation
_Data imputation is the process of dealing with missing values_. The proper methods depend on the type of data we are working with. Gereral methods include:

* Drop all records containing missing data.
* Heuristic-based: make a reasonable guess based on knowledge of the underlying domain.
* Mean Value: fill in missing data with the mean.
* Random Value
* Nearest Neighbor: fill in missing data using similar data points.
* Interpolation: use a method like linear regression to prodict the value of the missing data.

## Hierarchical Indexing
_Hierarchical indexing_ enables us to have multiple (two or more) index levels on an axis. Somewhat abstractly, it provides a way for us to work with higher dimensional data in a lower dimensional form.

* At times we will need to rearrange the order or **reorder** of the levels on an axis and **sort** the data by the values in one specific level.

* **Using columns as indexes**

## Combining and Merging Data Sets
If we find that our data set is insufficient to answer your questions, and we can't find one that is sufficient, it might still be possible to combine data sets to find ansers.

* **Merge**: connects rows based on one or more keys, overlapped columns or index.

* **Concatenate**: glues or stacks together objects along an axis.

* **Combine**: splices together overlapped data to fill in missing values in one object with values from another.

## Reshaping and Pivoting
These are a number of fundamental operations for rearranging tabular data. These data alternatingly referred to as _reshape_ or _pivot_ operations.

* **Stack**: rotates from the columns in the data to the rows.

* **Unstack**: rorates from the rows into the columns.

* **Pivot**: creates a _hierarchical index_ and then _unstack_ it. For examples, time-series data is commonly stored in databaese with _stacked format_. It's quite hard to work with this format, so we might prefer to have a table containing one column per distinct value and indexed by timestamps. The _pivot_ method help us that.

## Data Transformation
* **Remove duplicates**

* **Transform data using a function or mapping**: for many data sets, we may wish to perform some transformation based on the values in a array, list, dictionary, table,...

* **Replace values**

* **Rename axis indexes**

* **Bining**: Continuous data should be separated into _bins_ for analysis.

* **Detect outliers**

* **Permutation and random sampling**

* **Compute dummy**: transformation for statistical modeling or machine learning applications is coverting a categorical variable into _dummy_ or _indicator_ matrix.

## String Manipulation
* **String object methods**: _contains_,_split_, _join_, _index_, _count_, _replace_, _find with patters_, ...

* **Regular expressions**: provide a flexible way to search or match string patterns in text.

_Note_: when cleaning data, always maintain both the raw data and the cleaned versions. The raw data should be kept intact and preserved for future use. Any type of data cleaning/analysis should be done on a copy of the raw data.

_______________________

<div id='assessment'/>

# Data Assessment

It can be tempting to start developing a data-centric product or sophisticated statistical methods as soon as possible, but the benefits of getting to know our data are well worth the sacrifice of a little time and effort. If we know more about your data, we'll make more informed decisions at every step throughout our data science project and will reap the benefits later.

Even if we're confident that our data set contains what we think it contains, the data itself surely varies from one data point to another. Without a preliminary assessment, you may run into problems with outliers, biases, precision, specificity, or any number of other inherent aspects of the data. _In order to uncover these and get to know the data better, the first step of post-wrangling data analysis is to calculate some descriptive statistics_.

## Descriptive Statistics
A definition from Wikipedia:

> Descriptive statistics is the discipline of quantitatively describing the main features of a collection of information.

It's often hard to discuss descriptive statistics without mentioning inferential statistics. Inferential statistics is the practice os using the data we have to deduce - or infer - knowledge or quantities of which we don't have dirct measurements or data. With respect to a data set, we can say the following:

* Descriptive statistics asks, _"What do I have?"_

* Inferential statistics asks, _"What can I conclude?"_

Although descriptive and inferential statistics can be spoken of as two different techniques, the border between them is often blurry. In common sense, we would have to perform descriptive stat on the sample set in order to infer anything about the population, but it isn't always clear where the description stops ans where the inference starts.

### Why Do We Need It?
The purpose of calculating descriptive statistics at this stage in a data science project is to learn about your data set so that you understand its capabilities and limitations; trying to do anything but learn about our data at this point would be mistake. 

Complex statistical techniques such as those in machine learning, predictive analytics, and probabilistic modeling, for example, are completely out of the question for the moment. Complex methods like most of those used in machine learning today are not easily dissected or even understood. Random foresets, neural networks, and among others, may be understood in theory, but each of these has so many moving parts that one person (or a team) can't possible comprehend all of the specific pieces and values involved in obtaining a single result. Therefore, when we notice an incorrect result, even one that's grossly incorrect, it's not strightforward to extract from a complex model exactly which pieces contributed to this egregious error. More importantly, complex models that involve some randomness may not reproduce a specific error if you rerun the algorithm. It's always the better choice to us to stay close to our own data first before we allow any random processes or black boxes to draw conclusions for us.

In addition, there are always issues while wrangling the data, but it may have slipped past unnoticed, and some descriptive statistics can help us catch it now. 

One way to realize if we are still close to the data:

> We are close to the data if we are computing statistics that we are able to verify manually or that we can replicate exactly using another statiscal tool.

Staying close to the data ensures that we can be increadibly certain about these preliminary results, and keeping a set of good descriptive statistics with you throughout our project provides us an easy reference to compare with subsequent more relevant but more abstruse results that are the real focus of your project.

### Common Descriptive Statistics
There are 3 way to describe our data or more explicitly the distribution of our data.  

1. Centrality
2. Variability (Spread)
3. Shape

#### Centrality
* **Arithmetic Mean**: aka _Additive Mean_, it's just simply the average, so it has a severe effect of outliers
* **Geometric Mean**: aka _Multiplicative Mean_. It calculates averaging ratios and the effect of outliers on it is mild. Always less than arithmetic mean.
* **Median**: The median is the midpoint of the ordered dataset or the point that separates dataset in two equal pieces.
* **Mode**: Most frequent element in a dataset.

#### Variability
* **Variance** and **Standard Deviation**: Measure the dispersion of a set of data points around its mean value.
    * _Standard Deviation_ == sqrt(_Variance_)
    
* **Coefficient of variation (CV)**: Measure the ratio of dispersion of a single variable or multi-variables with different unit (e.g. usa-vnd).
    * _CV_ == _Standard Deviation_ / _mean_

#### Shape
* **Skewness**: Measure the asymmetry that indicates whether the observations in a dataset are concentrated on one side.
    * Positive: the outliers are to the right (long tail to the right in the distribution graph).
    * Negative: the outliers are to the left.

### Choosing Specific Descriptive Statistics to Calculate
Examples of helpful and informative descriptive statistics methods include but are not limited to the previous section. Any or all of these might be helpful in our project, and it's largely a matter of both preference and relevance when deciding which ones we might calculate in order to serve our goals.

It's not always obvious which statistics would be the best choice for our particular project, but we can ask ourselves a few questions what will lead to useful choices:

1. **How much data is there, and how much of it is relevant?**

This is usually fairly straightforward to answer. If the project concerns only a subset of the data, then we should find the totals for that subset as well. 

2. **What are the one or two most relevant aspects of the data with respect to project?**

Think about our project, lool at a few individual data points, and ask, "Which part do I care about the most?"

3. **Considering the most relevant aspects, what do typical data points look like?**

Take the answer to question 2 and calculate some summary statistics on the values corresponding to those aspects.

4. **Considering the most relevant aspects, what do the most extreme data points look like?**

This is similar question 3, but instead of looking at typical values, looks at extreme values such as maximum and minimum. When looking at extreme values, are there any values so hight or so lowe that they don't make sense? How many values are outside a reasonable range? For categorical or other non-numeric data, what are the most common and least common categories? Are all of these meaningful and useful to subsequent analysis?

## Exploratory Data Analysis
_Table and graphs_ can convey information more thoroughly and more quickly at times than pure text. Producing tables and graphs and keeping them for reference throughout your project is a good idea.

[_EDA_](https://en.wikipedia.org/wiki/Exploratory_data_analysis) is an approach, which is promoted by [John Tukey](https://en.wikipedia.org/wiki/John_Tukey): 

> to analyze data sets to summarize their main characteristics, _often with visual methods_. The statistical model can be used or not, but primarily EDA is for seeing what the data can tell us beyond the formal modeling or hypothesis testing task.

### Types of data
1. **Categorical**: FC (Man Utd, Barca, Real,..), Yes-No question, ...

2. **Numerical**

    * **Discrete**: SAT score, number of chidren we have,... 
    * **Continuous**: weight, height,...
    
### Graphs and Tables for Categorical
* **Frequency distribution tables**: Show the category and its corresponding absolute frequency.

* **Bar charts**: Each bar represents a category and on the y-axis we have the absolute frequency.

* **Pie charts**: Show the share of an item as a part of the total or relative frequency.

* **Pareto diagrams**: Represent 80/20 rule, the categories are shown in descending order of frequency, and a separate curve shows the cumulative frequency.

### Graphs and Tables for Numerical
* **Frequency distribution tables**: These ones for numberical variables are different than the ones for categorical. The tables are divided into intervals of equal length and show the absolute frequency of each interval. Interval witdth = (max - min) / number of desireed intervals.

* **Histogram**: Like bar charts, but for representing intervals.

### Graphs and Table for Relationships
1. Categorical
    
    * **Cross tables** (or continegency tables): On set of categories is labeling the rows and another is labeling the columns. We can fill in the table with the applicable data or relative frequencies.
    
    * **Side-by-side bar charts**: For showing cross tables.
    
2. Numerical
    
    * **Scatter plots**: Are useful for regression analysis, as the help us detect patterns (linearity, homoscedasticity).

## Check Assumptions about the Data
Whether we like to admit it or not, we all make assumptions about data sets. These assumptions about the data can be expectations or hopes, conscious or subconscious.

1. Assumptions about the contents of the data.

One specific thing to watch out for is missing data or placeholder values (NA, NaN,...). Most people tend to assume - or at least hope - that all fields in the data contain a usable value. It's always a good ideal to check whether such placeholder values occur often enough to cause problems

2. Assumptions about the distribution of the data

Bad things can happend if we assume we have normally distributed data and we don't. Statistical models that assume normal distributions don't handle outliers well, and the vast majority of popular statistical models make some sort of assumption of normality. Assuming normality when our data isn't even close can make the reuslts appear sigificant when in fact they're insignificant or plain wrong. All in all, although it might be OK to skip a statistical test for checking that our data fits a paricular distribution, do be careful and make sure that your data maches any assumed distribution at leaset roughly. Skipping this step can be catastrophic for results.

### A Handy Trick for Uncovering Our Assumptions
If we feel like we don't have assumptions, or we're not sure what they are, or even if we think we know all of that, try this: desccribe our data and project to anyone, who might be an outsider of the bussiness, what's in the data set and what we're going to do with it. Write down the description, then dissect it and look for assumptions.

For example,

* Description, 
    
    * Data: I'd gathered a dataset contains epidemic status of countries around the world and freedom indexes. 
    
    * Approach: I'm going to eastablish patterns of behavior over the country comparing correlation of epidemic status and freedom indexes. 
    
    * Conclusion: I'd like to draw conclusions about things like lower in rank of those indexes have better performance in response to epidemic."

* Dissect,

    * "Epidemic status of countries": Have we had all countries? May we consider about divide countries into continents or regions?
    
    * "Freedom indexes": Wich year did those indexes publish? and Do those indexes in that year affect to epidemic?
    
    * "Patterns of behavior": What assumptions do we have about what constitutes a pattern of behavior? Does every country need to engage in the same behavior in order for it to be declared a pattern, or do we have a set of patterns and we're looking for individual exmaples that match those patterns?
    
    * "Lower in rank": How to clairy which low or high?
    
    * "Performance in response to epidemic": How to detect the performance?

Realizing when we're making assumptions - by dissercting our project description and then asking such questions - can help us avoid many problems later. We wouldn't want to find our that a critical assumption was false only after we had completed the analysis, found odd results, and the gone back to investigate. Even more, we wouldn't want a critical assumption to be false and never notice it.

## Looking for Something Specific
One common goal in data science projects is to be able to find **entities** within our data set that **match a certain conceptual description**. The term entity is represented any unique individual represented in dataset. If we're working in:

* online retailing, we might consider customers as our main entities, and we might want to identify those who are likely to purchase a new video game system or a new book by a particular author. 

* advertising, we might be looking for people who are most likely to respond to a particular advertisement.

* finance, we might be looking for equities on the stock market that are about to increase in price.

If it were possible to perform a simple search for these characterizations, the job would be easy and we wouldn't need data science. The main challenge is to create a method of finding these interesting entities in a timely manner.

There are no guarantee that we would find the kind we were looking for, and also no guarantee that we would find any at all. One reason we might not find any is that there might not have been any.


