import pandas as pd
from sklearn.svm import SVR
import sklearn.metrics as metrics
from math import sqrt

def regression_results(y_test, y_pred):

    # Regression metrics
    explained_variance=metrics.explained_variance_score(y_test, y_pred)
    mean_absolute_error=metrics.mean_absolute_error(y_test, y_pred)
    mse=metrics.mean_squared_error(y_test, y_pred)
    mean_squared_log_error=metrics.mean_squared_log_error(y_test, y_pred)
    median_absolute_error=metrics.median_absolute_error(y_test, y_pred)
    r2=metrics.r2_score(y_test, y_pred)

    print('explained_variance: ', round(explained_variance,2))
    print('mean_squared_log_error: ', round(mean_squared_log_error,2))
    print('r2: ', round(r2,2))
    print('mean_absolute_error: ', round(mean_absolute_error,2))
    print('MSE: ', round(mse,2))
    print('RMSE: ', round(sqrt(mse),2))
    print('median_absolute_error:', round(median_absolute_error,2))



# read in csv files
X_train = pd.read_csv('train.csv')
y_train = pd.read_csv('y_train.csv', names=['price'])

X_test = pd.read_csv('test.csv')
y_test = pd.read_csv('y_test.csv', names=['price'])

# drop features
X_train = X_train.drop(['latitude', 'longitude', 'instant_bookable_f', 'room_type_Entire home/apt','room_type_Private room','room_type_Shared room'], axis=1)
X_test = X_test.drop(['latitude', 'longitude', 'instant_bookable_f','room_type_Entire home/apt','room_type_Private room','room_type_Shared room'], axis=1)

# some exploratory data analyses

print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)

#print(X_train.info())
#print(X_train.describe())
#print(X_train.head())


# fit Regressor to training data
sv_reg = SVR()
sv_reg.fit(X_train, y_train)

# Make predictions
y_pred = sv_reg.predict(X_test)

# compute metrics
regression_results(y_test, y_pred)


