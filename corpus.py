# -*- coding:utf-8 -*-
import os
import re

class Corpus:
    def __init__(self, filepath):
        root_path = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.normpath(os.path.join(root_path, filepath))
        re_split = re.compile("\s+")
        self.pos_doc_list = []
        self.neg_doc_list = []
        #读取语料库，1表示积极，0表示消极
        with open(filepath) as f:
            for line in f:
                splits = re_split.split(line.strip())
                if splits[0] == '1':
                    self.pos_doc_list.append(splits[1:])
                elif splits[0] == '0':
                    self.neg_doc_list.append(splits[1:])
                else:
                    raise ValueError("Corpus Error")
        #确保积极语料库和消极语料库一样多
        self.doc_length = len(self.pos_doc_list)
        assert len(self.neg_doc_list) == len(self.pos_doc_list)
        #如果未指定训练数据，默认为0
        self.train_num = 0

    def get_corpus(self, start=0, end=-1):
        assert self.doc_length >= self.train_num
        if end == -1:
            end = self.doc_length
        data = self.pos_doc_list[start:end] + self.neg_doc_list[start:end]
        data_labels = [1] * (end - start) + [0] * (end - start)
        return data, data_labels

    def get_train_corpus(self, num):
        self.train_num = num
        return self.get_corpus(end=num)

    def get_all_corpus(self):
        data = self.pos_doc_list[:] + self.neg_doc_list[:]
        data_labels = [1] * self.doc_length + [0] * self.doc_length
        return data, data_labels

class CommentCorpus(Corpus):
    def __init__(self):
        Corpus.__init__(self, "Corpus/comment.txt")