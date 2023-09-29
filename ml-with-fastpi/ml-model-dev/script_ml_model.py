# %% [markdown]
# # Bank Note Authentication ML Model Development

# %% [markdown]
# - Dataset Link: https://www.kaggle.com/datasets/shantanuss/banknote-authentication-uci/

# %%
import pandas as pd
import numpy as np

# %% [markdown]
# ### Load Dataset

# %%
df = pd.read_csv('BankNoteAuthentication.csv')

# %%
df

# %% [markdown]
# #### Define feature names

# %%
feature_names = ['variance', 'skewness', 'curtosis', 'entropy']

# %% [markdown]
# ### Independent and Dependent features

# %%
X = df[feature_names]
y = df['class']

# %%
X.head

# %%
y.head

# %% [markdown]
# ### Train Test Split Data

# %%
from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# %% [markdown]
# ### Implement Model: Random Forest Classifier

# %%
from sklearn.ensemble import RandomForestClassifier


# Create the RandomForestClassifier
classifier = RandomForestClassifier()

# Fit the classifier
classifier.fit(X_train, y_train)

# Set the feature_names attribute after fitting
classifier.feature_names = feature_names

# %% [markdown]
# #### Prediction

# %%
y_pred = classifier.predict(X_test)

# %% [markdown]
# #### Check Accuracy of the model

# %%
from sklearn.metrics import accuracy_score

score = accuracy_score(y_test, y_pred)
score

# %% [markdown]
# ### Create a Pickle File Using Serialization

# %%
import pickle
pickle_out = open("ml_model.pkl", "wb")
pickle.dump(classifier, pickle_out)
pickle_out.close()

# %% [markdown]
# ### Test the Model Prediction Output

# %%
# Ignore the warning
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

classifier.predict([[100,50,4,70]])


