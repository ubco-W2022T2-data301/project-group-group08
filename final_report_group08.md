# Introduction 
Since we are living in a generation where technology is advancing rapidly, this may lead to an unhealthy lifestyle for humanity. Through this poject, we hope to raise awareness and promote a healthy lifestyle by showcasing the underlying factors of high healthcare charges in the US. We believe that these and other supporting visualizations and information will be very beneficial for the audience to understand the impact of unhealthy lifestyle towards their medical bill.

# Exploratory Data Analysis 
A summary of the highlights of your EDA, where you can show some visualizations of the exploratory data analysis your group did.

The main dataset we are analyzing is the Medical Cost Personal Datasets was taken from Kaggle. The dataset contains 7 columns - age, sex, BMI, children, smoker, region and charges. The supporting dataset we used is the Adult Census Income; the dataset contains 15 columns - age, workclass, fnlwgt (final weight), education, education.num, marital.status, occupation, relationship, race, sex, capital.gain, capital.loss, hours.per.week, native.country, and income. With these, we were able to create different visualizations that helped us produce 

# Question 1 + Results 
**What are the average healthcare costs for different age groups?**
![](images/Amierq1barplot.png) 
Since this is a barplot it is hard to see the trend between age group and average healthcare cost. However, by eye, we can see an overall positive trend if we compare the peaks of the barcharts for all ages. But the bar plot is useful as we are able to see some bars where the average cost increases a lot or decreases a lot. For example, from age 37 to age 38, the average cost drops by nearly $10,000. However, because we aren't able to look into the sample for age 37, we don't know why the average medical cost for that group is so high.

![](images/Amierq1regplot.png)
From Tableau, we are able to confirm our insights of an overall positive trend between Age and average medical cost. As shown through the statistical summary tab, the R-squared value is 0.7 which shows a strong positive correlation between both factors. Thus, as predicted, as we get older, it is possible for the average cost to get higher because older people are prone to more diseases.

# Question 2 + Results 
Clearly state your research question, and include 2-3 visualizations that helped you answer your research question. You can create multi-panel figures, but each of your visualizations must speak directly to your research question, and any insights you were able to get from it should be clearly articulated in the figure caption/description.

# Question 3 + Results 

**What is the correlation between BMI and Medical Charges for smokers and non-smokers**

<img src="images/kennnosmokebar.png" width= 50%><img src="images/kennsmokebar.png" width= 50%>
From the two scatterplots above, we can see that between BMI and Charges, the smoker graph has a very strong positive correlation (0.806) with the there being two major density 'blocks' seen.
the non-smoker graph (0.084) has a very weak or no correlation where the plots are very concentrated under $15000 charges and across the whole range of the BMI. The results could be due to smoking increases the severity and health risks associated with higher BMI's

**Which region has a higher percentage of smokers? Does this highly affect the average BMI and Charges?** 

<img src="images/kennnumsmoker.png" width= 60%>

<img src="images/kennbmiviolin.png" width= 50%><img src="images/kennchargesviolin.png" width= 50%>
Southeast (33.4) and Southwest (30.6) regions both have higher average BMI's as compared to the northeast (29.17) and northwest (29.19) regions. The trend continues for the southeast region where they have the highest average medical charges (14735) and the southwest region having the lowest medical average charges (12346). It seems like the medical cost do follow the hypothesis where the larger number of smokers in a population increases medical charges but the same does not apply to BMI where the southern regions have a higher average BMI as compared to the northern regions.

# Summary/Conclusion 
A brief paragraph that highlights your key results and what you learned from doing this project.

After researching, it is clear that there are many factors of hgh healthcare charges. In addition, most of these factors are related to each other causing some factors to be more significant once analyzed against other factors. From the plots shown throughout, we can see that age is a significant factor towards high healthcare charges because as we get older, we are prone to more diseases. Whilst bmi becomes more significant once we separate it into smokers and non-smokers and thus showing that smokers are more likely exposed to health risks which causes healthcare charges to be higher than non-smokers. Through this project, we learnt to use pandas and data visualization tools to create 