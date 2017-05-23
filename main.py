# -*- coding:utf-8 -*-
from feature_extraction import ChiSquare
from classifiers import SVMClassifier
from corpus import CommentCorpus

class Train:
    def __init__(self, train_num, feature_num, C, corpus):
        self.train_num = train_num
        self.feature_num = feature_num
        self.C = C

        # 获取语料库
        self.train_data, self.train_labels = corpus.get_train_corpus(train_num)

        # 特征提取
        feature = ChiSquare(self.train_data, self.train_labels)
        self.best_words = feature.best_words(feature_num)

    def svm(self):
        svm_obj = SVMClassifier(self.train_data, self.train_labels, self.best_words, self.C)
        return svm_obj

def main():
    train_num = 1000
    feature_num = 800
    C = 150
    corpus = CommentCorpus()
    train = Train(train_num, feature_num, C, corpus)
    svm_obj = train.svm()
    while True:
        print u"请输入餐厅评论语句："
        sentence = raw_input()
        if not sentence:
            print u"请输入有效评论！\n"
            continue
        result = svm_obj.classify(sentence)
        if result == 1:
            print u"恭喜您！这是一条积极评论！"
        else:
            print u"很抱歉！这是一条消极评论！"

if __name__ == "__main__":
    main()
