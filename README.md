# -influenza-like-illness-ILI-in-Italy
The goal of this assignment is trying to estimate, in near-real time, the level of influenza-like illness (ILI) in Italy by monitoring the rate of particular Wikipedia article views on a daily basis. We calculated the number of times certain influenza- or health-related Wikipedia articles were accessed each day between July 2015 and Decemcer 2018 and compared these data to official ILI activity levels provided by Influnet (Rete Italiana Sorveglianza Influenza).

##Introduction 

The goal of this assignment is trying to estimate, in near-real time, the level of influenza-like illness (ILI) in Italy by monitoring the rate of particular Wikipedia article views on a daily basis. We calculated the number of times certain influenza- or health-related Wikipedia articles were accessed each day between July 2015 and Decemcer 2018 and compared these data to official ILI activity levels provided by Influnet (Rete Italiana Sorveglianza Influenza).

To this end, we have created a method of estimating current ILI activity in Italy by gathering information on the number of times particular Wikipedia articles have been viewed. Wikipedia is a massive, user-regulated, online encyclopedia.

The purpose of this assignment is to develop a statistical model to provide near real-time estimates of ILI activity in Italy using freely available data gathered from the online encyclopedia, Wikipedia.

Folder_structure

-Python Notebook

-influnet - [contains the PDF files from influnet survivelence system. We are considering the data of 2015-16, 2016-17, 2017-18 for our analysis]

-wiki - [contains the all the data collected from wikipedia based on the pages that we selected for our analysis]



## Consolidation of results

Below are the results we obtained,

3.1 -
Multiple linear regression - Mean squared error: 0.18 Variance score: 0.89
LASSO - Mean squared error: 0.06 Variance score: 0.94

3.2 -
Multiple linear regression - Mean squared error: 1.23 Variance score: -0.23
LASSO - Mean squared error: 0.06 Variance score: 0.94

As we can observe, with the actual dataset both the regression model performed comparitively well with LASSO having the best performance. 

With new features (pertaining to preceeding weeks data) added the performance of the multiple linear regression model decreased multiflold where as the 
performance of the LASSO model remained the same irrepective of the new features. 
so we conclude our regression analysis that, for good prediction performance of the Influnet prevalence LASSO is a good choice
