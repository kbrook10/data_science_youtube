## Notes -> Training tutorial via https://www.youtube.com/watch?v=T5pRlIbr6gg - Siraj Raval

# Import dependencies (i.e. Use tree module to display decision trees with dataset)
from sklearn import tree


# Create variable to 
clf = tree.DecisionTreeClassifier()

# CHALLENGE - create 3 more classifiers...
# 1
# 2
# 3

# Create Dataset to use with Decision Tree...Create a list of lists for the height, weight and shoe size
# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]


# Create a list of body metrics that are associated with the X values above...This example is a list of strings
Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']


# Train model on above dataset
clf = clf.fit(X,Y)

# Predict the Gender based on user input (i.e. create variable and use predict() method to predict gender)

prediction = clf.predict([[154,54,37]])

# Run predictions

print prediction