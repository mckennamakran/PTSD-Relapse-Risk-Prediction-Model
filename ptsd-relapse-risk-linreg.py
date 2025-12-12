import pandas as pd
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt


#load the dataset
data = pd.read_csv('PTSD_Relapse_Risk.csv')

df = DataFrame(data)

#print the feature names
print(df.columns,'\n')

#declare x & y variables
X = df.drop('Relapse_Risk_Score', axis=1) #all the data except the target column
Y = df['Relapse_Risk_Score'] #the target column

#convert categorical data into numeric
X = pd.get_dummies(X, drop_first=True)

#check the number of rows and columns in each
print("Shape of features (X):", X.shape)
print("Shape of target (y):", Y.shape, "\n")

#split the data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

#model
model = LinearRegression()
model.fit(X_train, Y_train)

#predictions
predictions = model.predict(X_test)
print("First 10 predictions:", predictions[:10], "\n")

def risk_category(score):
    if score <= 20:
        return "Very Low"
    elif score <= 40:
        return "Low"
    elif score <= 60:
        return "Moderate"
    elif score <= 80:
        return "High"
    else:
        return "Very High"

predicted_risks = []

for score in predictions[:10]:
    category = risk_category(score)
    predicted_risks.append(category)

for i, category in enumerate(predicted_risks):
    print(f"Patient {i+1}: {category}")

print(predicted_risks)

#detemrmine accuracy
mse = mean_squared_error(Y_test, predictions)
r2 = r2_score(Y_test, predictions)

print("Mean Squared Error (MSE):", round(mse, 2))
print("R² score:", round(r2, 2), "\n")

coef_df = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
}).sort_values(by="Coefficient", key=abs, ascending=False)

print("Feature coefficients:\n", coef_df)

#visual of predicted vs actual relapse risk
plt.figure(figsize=(8,6))
plt.scatter(Y_test, predictions, color='pink', edgecolor='red')
plt.plot([min(Y_test), max(Y_test)], [min(Y_test), max(Y_test)], color='black', linestyle='--')
plt.title("Predicted vs Actual Relapse Risk", fontsize=14)
plt.xlabel("Actual Relapse Risk", fontsize=12)
plt.ylabel("Predicted Relapse Risk", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
