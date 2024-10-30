import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

X_data = pd.read_csv("out.csv")
y_data = pd.read_csv("final.csv")


def label_preprocessing(placeholder_variable):
    if placeholder_variable == "Yes":
        return 1
    if placeholder_variable == "No":
        return 0
    if placeholder_variable == "Yes(Detected Positive)":
        return 1
    if placeholder_variable == "No(Detected Negative)":
        return 0


y_data = y_data.result.apply(label_preprocessing)

X_train, X_test, y_train, y_test = train_test_split(
    X_data, y_data, random_state=3, test_size=0.1
)


def training_model():
    knn_model = KNeighborsClassifier(n_neighbors=2)
    knn_model.fit(X_train, y_train)
    return knn_model


# knn_model = training_model()
# y_pred = knn_model.predict(X_test.values)
#
# accuracy = accuracy_score(y_test, y_pred)
# print("Accuracy:", accuracy)
