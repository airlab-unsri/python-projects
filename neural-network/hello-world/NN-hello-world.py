from sklearn.neural_network import MLPClassifier
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = [0, 0, 1, 1]
clf = MLPClassifier()
clf = clf.fit(features, labels)
print(clf.predict([[150, 0]]))
