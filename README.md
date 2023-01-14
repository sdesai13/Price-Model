# Price-Model

Machine Learning model to predict house prices in the GTA based on location (Toronto,Vaughan,Brampton,Missisauga) and how many beds/baths the house has.

Used decision tree regression to create an initial model, then used grid search to tune the parameters to create a tuned decision tree regression model.

Also trained an XgBoost regressor model, which was the most accurate model! 

# Data collection

Scraped data of over 300 houses using beautifulsoup and Python from real-estate websites, and then processed and stored the data into a list of tuples. I then used Pandas to write the data into a csv, after which I was able to train my models on it.
