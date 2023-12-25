# STACKOVERFLOW ANALYSIS USING STACK EXCHANGE API
This Python-based project utilizes the Stack Exchange API to analyze StackOverflow data, focusing on the 'R' and 'Dot Net' programming tags. The analysis, divided into data extraction and visualization scripts, explores five key metrics—Is Answered, View Count, Answer Count, Score, and Reputation. Additional analysis highlights distinct patterns in answer resolution between the two tags. The project provides valuable insights into the dynamics of these programming communities on StackOverflow.

## Language(s) used -

- Python

## Identifier for a post -

- **Question Id (question\_Id) -** Id of the question.

## Files and Folders -

- **soDataExtraction.py -** used to extract the data from stackoverflow and generate csv files.
- **soVisualization.py -** used to generate plots using the csv files generated.
- **plots -** contains png file of all the plots generated.

## PART 1 - PLOTS TO UNDERSTAND DIFFERENCES IN DISTRIBUTION OF THE 5 METRICS BETWEEN THE POSTS OF THE TWO TAGS

### 1. Is Answered (is\_answered)

It is a boolean value which indicates whether the question has been answered or is still

open.

![alt text](https://github.com/iamber12/stackOverflowAnalysis/blob/main/plots/is_answered.png)

**Above plot shows the number of answers/unanswered posts for the 2 tags.**

**Analysis -**

Based upon the above plot we can infer that -

- Total questions answered for posts having &#39;R&#39; tag are greater than those of the &#39;Dot Net&#39; tag which depicts that the contributors on Stackoverflow who belong to the R community, are more adept in their field as compared to Dot Net community.
- This could possibly suggest that R contributors are more active than Dot Net contributors.
- Another analysis could be that, since it&#39;s a 6 month data, it takes more time for contributors to answer questions related to Dot Net tag than R tag.

### 2. View Count (view\_count)

It is a numeric value which shows the number of views on a post.

![alt text](https://github.com/iamber12/stackOverflowAnalysis/blob/main/plots/view_count.png)

**Above plot shows the number of posts lying in various buckets as defined in the legend for 2 tags.**

**Analysis -**

Based upon the above plot we can infer that -

- For the majority of questions for both R and Dot Net tag, the view count is less than or equal to 150. This implies that contributors related to both tags are equally active when it comes to viewing the posts.
- However, speaking of outliers in Dot Net tag, this suggests that while Dot Net contributors are more widespread, they are not very consistent in using Stackoverflow as a platform but are only focussed towards certain questions of their interest.

### 3. Answer Count (answer\_count)

It is a numeric value which shows the number of answers on a question.

![alt text](https://github.com/iamber12/stackOverflowAnalysis/blob/main/plots/answer_count.png)

**Above plot shows the number of questions which have a specific answer count as defined in the legend for 2 tags.**

**Analysis -**

Based upon the above plot we can infer that -

- In terms of answering the questions, contributors who are familiar with R are much more active, with the majority of the questions having greater than or equal to 1 answer than those who are familiar with Dot Net, who have the majority answer count of 0 or 1.
- The above point supports our hypothesis made in metric 1 as well, that contributors who are familiar with R are more active.

### 4. Score (score)

It is a numeric value which shows the difference between number of up-votes and number of down-votes on a question.

![alt text](https://github.com/iamber12/stackOverflowAnalysis/blob/main/plots/score.png)

**Strip plot of scores of questions for 2 tags**

**Analysis -**

Based upon the above plot we can infer that -

- Distribution of score for both the tags is almost same, with majority of them lying in the range 0-5. This implies that contributors for both the tags are consistently active when it comes to up-voting/down-voting the posts which is a good sign as this helps the community to solve the questions quickly.

### 5. Reputation (reputation)

It is a numeric value which shows the reputation of the owner of the question. It is a

rough measurement of how much the community trusts the user.

![alt text](https://github.com/iamber12/stackOverflowAnalysis/blob/main/plots/reputation_1.png)

**Fig 1 - Mean of reputation of owners of the questions for 2 tags**

![alt text](https://github.com/iamber12/stackOverflowAnalysis/blob/main/plots/reputation_2.png)

**Fig 2 - Cat plot of owners of the questions for 2 tags**

**Analysis -**

Based upon the above plots we can infer that -

- Fig 1 - Mean of reputation of the owner of posts related to Dot Net tag is ~2600 whereas for R tag, it is ~1300. However, Fig 2 suggests that since the reputation of the owners of posts related to Dot Net tag seems to have more outliers as compared to R, the mean is deflected.
- As we have seen above in metric 2, contributors related to Dot Net seem to have only a certain set of users who are highly active and are more engrossed while the majority of users lie in a range of 0-12.5k owner reputation which is similar to where the major portion of R contributors lie in.

## PART 2 - ADDITIONAL ANALYSIS

![alt text](https://github.com/iamber12/stackOverflowAnalysis/blob/main/plots/additional.png)

**Above plot shows the relationship between Answer Count and Is Answered metrics for questions related to 2 different tags**

Based upon the above plot, we can infer that it usually takes 1 or 2 answers for the contributors to answer questions having &#39;R&#39; tag. However, this number increases to 3 for questions with the &#39;Dot Net&#39; tag. This aligns with our findings of metric 1 that R contributors are more adept as compared to Dot Net contributors.
