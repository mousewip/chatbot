#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.externals import joblib
import os
from sklearn import metrics
from src.model.naive_bayes_model import NaiveBayesModel
from src.model.svm_model import SVMModel

APP_ROOT = os.path.dirname(__file__)


class TextClassificationPredict(object):
    def __init__(self):
        self.test = None
        if os.path.isfile(APP_ROOT + '/model.sav'):
            self.model = joblib.load(APP_ROOT + '/model.sav')
        if os.path.isfile(APP_ROOT + '/model_conv.sav'):
            self.model_conv = joblib.load((APP_ROOT + '/model_conv.sav'))
        print('Load all model success')

    def get_model(self):
        return self.model

    def predict(self, pred_text):
        test_data = []
        test_data.append({"question": pred_text, "intent": ""})
        df_test = pd.DataFrame(test_data)
        predicted = self.model.predict(df_test["question"])

        # Print predicted result
        print(predicted)
        result = predicted[0]
        proba = self.model.predict_proba(df_test["question"])
        accu = max(proba[0])
        return result, accu * 100

    def predict_conv(self, pred_text):
        test_data = []
        test_data.append({"question": pred_text, "intent": ""})
        df_test = pd.DataFrame(test_data)
        predicted = self.model_conv.predict(df_test["question"])

        # Print predicted result
        print(predicted)
        result = predicted[0]
        proba = self.model_conv.predict_proba(df_test["question"])
        accu = max(proba[0])
        return result, accu * 100

    def train_model_conv(self):
        df_train = pd.read_excel('conv.xlsx', encoding='utf8')

        test_data = []
        test_data.append({"question": "dm mày", "intent": "unknown"})
        df_test = pd.DataFrame(test_data)
        # init model naive bayes
        model = NaiveBayesModel()
        clf = model.clf.fit(df_train["question"], df_train.intent)
        joblib.dump(clf, 'model_conv.sav')
        predicted = clf.predict(df_test["question"])
        # Print predicted result
        print(predicted)
        print(clf.predict_proba(df_test["question"]))

    def train_model(self):
        #  train data
        df_train = pd.read_json('sk.json', encoding='utf8')

        test_data = []
        test_data.append({"question": "tôi bị đau bụng", "intent": "đau ruột thừa"})
        df_test = pd.DataFrame(test_data)

        # init model naive bayes
        model = NaiveBayesModel()
        print('begin train model')
        clf = model.clf.fit(df_train["question"], df_train.intent)
        joblib.dump(clf, 'model.sav')
        predicted = clf.predict(df_test["question"])
        # Print predicted result
        print(predicted)
        print(clf.predict_proba(df_test["question"]))


if __name__ == '__main__':
    tcp = TextClassificationPredict()

    if not os.path.isfile("model.sav"):
        tcp.train_model()
        print("Train model success")
    else:
        model = joblib.load('model.sav')
        #  test data
        test_data = []
        test_data.append({"question": "hoa mắt", "intent": "cận thị"})
        df_test = pd.DataFrame(test_data)
        predicted = model.predict(df_test["question"])

        # Print predicted result
        print(predicted)

        ls = model.predict_proba(df_test["question"])
        # print(ls[0])
        print("accuracy:  %0.3f" % max(ls[0]))

        score = metrics.accuracy_score(df_test.intent, predicted)
        print("accuracy:   %0.3f" % score)
        while True:
            inp = input("> ")
            test_data = []
            test_data.append(
                {"question": inp, "intent": ""})
            df_test = pd.DataFrame(test_data)
            predicted = model.predict(df_test["question"])
            ls = model.predict_proba(df_test["question"])
            print(predicted[0])
            print("accuracy: %.2f" % (max(ls[0] * 100)))
