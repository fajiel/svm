# -*- coding:utf-8 -*-
import numpy as np
from sklearn.svm import SVC

class SVMClassifier:
    def __init__(self, train_data, train_labels, best_words, C):
        train_data = np.array(train_data)
        train_labels = np.array(train_labels)

        self.best_words = best_words
        self.clf = SVC(C=C)
        self.__train(train_data, train_labels)

    def words2vector(self, all_data):
        vectors = []
        for data in all_data:
            vector = []
            for feature in self.best_words:
                vector.append(data.count(feature))
            vectors.append(vector)

        vectors = np.array(vectors)
        return vectors

    def __train(self, train_data, train_labels):
        print u"SVM模型开始训练，请耐心等待！"
        train_vectors = self.words2vector(train_data)
        self.clf.fit(train_vectors, np.array(train_labels))
        print u"SVM模型训练结束!"

    def classify(self, data):

        vector = self.words2vector([data])
        prediction = self.clf.predict(vector)

        return prediction[0]