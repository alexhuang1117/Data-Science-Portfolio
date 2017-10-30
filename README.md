# Data Science Portfolio

This is a repository of the projects I worked on or currently working on. It is updated regularly. The projects are either written in R (R markdown) or Python (Jupyter Notebook). The goal is to use data science/statistical modelling techniques to find something that is interesting. A typical project consist of finding and cleaning data, analysis, visualization and conclusion.

## Projects:

###  [Bitcoin Price Analysis](https://github.com/alexhuang1117/Data-Science-Portfolio/blob/master/Bitcoin_Analysis/Bitcoin_Analysis.md)
* Plot Bitcoin Price vs S&P500 prices, and perform Granger Causality test.
* Fitted ARIMA model on Bitcoin prices to forecast Bitcoin range of movement.
* Keywords(R, Time Series, Causality)
![](https://github.com/alexhuang1117/Data-Science-Portfolio/blob/master/Bitcoin_Analysis/Bitcoin_Analysis_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-21-1.png)

###  [Exchange Rate Analysis During US Election - Under Construction](https://github.com/alexhuang1117/Data-Science-Portfolio/blob/master/FX_Analysis_During_US_Election/main.ipynb)
* In this project, I tried to predict US (2016) election victories as the voting results of each region becomes available.
* The prior information is the polling data and as each regions results comes out, the model is updated.
* Monte Carlos simulation is used to simulate the winner of the election.
* The result is compared with exchange rates fluctuations to see how the financial market kept up with the result.
* Keywords(Python, Linear Regression, Monte Carlos Simulation)

###  [Exchange Rate Analysis During UK Election - Under Construction](https://github.com/alexhuang1117/Data-Science-Portfolio/blob/master/FX_Analysis_during_UK_Election/main.ipynb)
* In this project, I tried to predict UK (2017) election victories as the voting results of each region becomes available.
* Timing of announcement of each region is retrieved from Twitter using announcement tweet timestamp
* The prior information is the polling data and as each regions results comes out, the model is updated.

* Keywords(Python, Twitter API, Merging Data)


###  [Power-law or Log-normal? Baby Name and Twitter Analysis](https://github.com/alexhuang1117/Data-Science-Portfolio/blob/master/Power_Law_vs_Lognormal_US_Babynames/Power_Law_vs_Lognormal_US_Babynames.md)
* Fitted power-law and log-normal distribution to US baby names since 1960 and compared the fit.
* Use bootstrapping techniques to find a distribution of the power-law parameters
* Crawled Twitter to find 20000 random user and fitted power law distribution to users' friends count and followers count.
* Keywords(R, Power-law, Bootstrapping, Log-normal)
 ![](https://github.com/alexhuang1117/Data-Science-Portfolio/blob/master/Power_Law_vs_Lognormal_US_Babynames/Power_Law_vs_Lognormal_US_Babynames_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-7-1.png)
  
### [Comparing Ridge and Lasso Regularization with Cross Validation](https://github.com/alexhuang1117/Data-Science-Portfolio/blob/master/Ridge_Lasso_CV_Comparison/main.ipynb)
* Fitted polynomial linear regression on wine quality vs wine chemical properties.
* Used ridge and lasso regularization to tackle overfitting and compared result
* Used cross validation to select the optimal regularization strength
* Keywords(Python, Linear Regression, Ridge and Lasso Regularization, Cross Validation) 
 
 
### [Twitter Sentiment Daily and Weekly Fluctuations](https://github.com/alexhuang1117/Data-Science-Portfolio/blob/master/Twitter_Sentiement_Analysis/Twitter_sentiment_Analysis.md)
* Parsed a few GB of Tweets to select all the tweets in UK and in English.
* Used 'qdap' package to analyze the emotion of the Tweets
* Plotted the emotions over the day and over the week and analysed the interesting results.
* Keywords(R, Twitter API, Time Series, Sentiment Analysis, ggplot)
 ![](https://github.com/alexhuang1117/Data-Science-Portfolio/blob/master/Twitter_Sentiement_Analysis/Twitter_sentiment_Analysis_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-7-2.png)
  
  
### [GDP and Future Orientation](https://github.com/alexhuang1117/Data-Science-Portfolio/blob/master/GDP%20and%20Future%20Orientation/GDP_and_Future_Orientation.md)
* Downloaded economic indicators using World Bank API, and cleaned data
* Downloaded seach query of next and last year in Google for each country
* Fitted linear regression between GDP and future orientation
* keywords(R, World Bank API, Google API, Data Cleaning, Linear regression)
![](https://github.com/alexhuang1117/Data-Science-Portfolio/blob/master/GDP%20and%20Future%20Orientation/GDP_and_Future_Orientation_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-8-1.png)



