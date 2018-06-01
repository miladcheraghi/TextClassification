import preprocessing
import nltk
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier


print("Cleaning and parsing the training set telegram post...\n")
cleanTrain = []
train = pd.read_json('LabeledTrainedData.json')

for i in range(0,len(train)):
    cleanTrain.append(preprocessing.postToWord(train["text"][i]))
    if (i % 1000 == 0):
        print("Post %d of %d...\n" % (i, len(train)))
        # print(cleanTrain[i])

print("**************************")
print("cleanTrain Ok...")
print("**************************")

# Initialize the "CountVectorizer" object, which is scikit-learn's
# bag of words tool.
vectorizer = CountVectorizer(analyzer = "word",tokenizer = None,preprocessor = None,stop_words = None,max_features = 5000)

# transform training data into feature vectors
trainDataFeatures = vectorizer.fit_transform(cleanTrain)

# convert the result to an Numpy array
trainDataFeatures = trainDataFeatures.toarray()

print(trainDataFeatures.shape)

# vocab = vectorizer.get_feature_names()
# print(vocab)

print("Training the random forest...")

# Initialize a Random Forest classifier with 100 trees
forest = RandomForestClassifier(n_estimators = 100)

# Fit the forest to the training set, using the bag of words as
# features and the sentiment labels as the response variable
#
# This may take a few minutes to run
forest = forest.fit( trainDataFeatures, train["class"] )

# Read the test data
test = pd.read_json('TestData.json')

# Verify that there are 25,000 rows and 2 columns
print(test.shape)

# Create an empty list and append the clean reviews one by one
numTest = len(test["text"])
cleanTest = []

print("Cleaning and parsing the test set movie reviews...\n")
for i in range(0,numTest):
    cleanTest.append( preprocessing.postToWord(test["text"][i]) )
    if( i % 1000 == 0 ):
        print("Review %d of %d\n" % (i+1, numTest))


# Get a bag of words for the test set, and convert to a numpy array
testDataFeatures = vectorizer.transform(cleanTest)
testDataFeatures = testDataFeatures.toarray()

# Use the random forest to make sentiment label predictions
result = forest.predict(testDataFeatures)

print("Result Is Ok.")

# Copy the results to a pandas dataframe with an "id" column and
# a "class" column
output = pd.DataFrame( data={"_id":test["_id"], "class":result} )

# Use pandas to write the comma-separated output file
output.to_csv( "Result.csv", index=False, quoting=3 )
