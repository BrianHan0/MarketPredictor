from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score
from data_fetcher import get_stock_data
import pandas as pd

data = get_stock_data("AAPL")
model = RandomForestClassifier(n_estimators=100, min_samples_split=100, random_state=1)

train = data.iloc[:-100]
test = data.iloc[-100:]

predictors = ["Close", "Volume", "Open", "High", "Low"]
model.fit(train[predictors], train["Target"])


prediction = model.predict(test[predictors])
preds = pd.Series(prediction,index=test.index)
precision_score(test["Target"], preds)

combined = pd.concat([test["Target"], preds], axis=1)
combined.plot()

`

