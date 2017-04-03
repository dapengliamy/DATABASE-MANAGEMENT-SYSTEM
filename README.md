**Data Collection**

We used scrapy to crawl raw data on Craigslist in Corvallis, after data cleaning, we implemented MySQL queries to join and project with two schemas. The features of the aparemtns are location(longitude, latitude), safety and size of the apartment. 
There are 606 training examples and 50 testing examples.
Linear Regression and Neural Network Regression Models are trained to fit the training data set. 

**Result**

The score for the neural network regression model is 73.3% which is better than the linear regression model(69.9%). Predict_combine.csv shows part of our result of the predicted data. The left column shows the predicted price of the linear regression model, the right column shows the predicted price of the neural network regression model and the middle column shows the true predicated price. This table clearly demonstrates the more accuracy neural network models achieved in predicating the price compared to the linear regression model.