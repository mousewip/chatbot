#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from src.model.naive_bayes_model import NaiveBayesModel
from sklearn.externals import joblib
import os
from sklearn import metrics

APP_ROOT = os.path.dirname(__file__)
class TextClassificationPredict(object):
    def __init__(self):
        self.test = None
        self.model = joblib.load(APP_ROOT + '/model.sav')
        print('Load model success')

    def get_model(self):
        return self.model

    def get_train_data(self):
        #  train data
        df_train = pd.read_json('sk.json', encoding="utf-8")

        #  test data
        test_data = []
        test_data.append({"feature": "nhìn mờ các đối tượng ở xa.", "target": "cận thị abc"})
        df_test = pd.DataFrame(test_data)

        # init model naive bayes
        model = NaiveBayesModel()

        clf = model.clf.fit(df_train["feature"], df_train.target)

        joblib.dump(clf, 'model.sav')

        predicted = clf.predict(df_test["feature"])

        # Print predicted result
        print(predicted)
        print(clf.predict_proba(df_test["feature"]))

    def predict(self, pred_text):
        test_data = []
        test_data.append({"feature": pred_text, "target": ""})
        df_test = pd.DataFrame(test_data)
        predicted = self.model.predict(df_test["feature"])

        # Print predicted result
        print(predicted)
        result = predicted[0]
        proba = self.model.predict_proba(df_test["feature"])
        accu = max(proba[0])
        return 'Có thể bạn đang bị: {res}\nĐộ tin cậy: {per}%'.format(res=result, per=accu * 100)


if __name__ == '__main__':
    tcp = TextClassificationPredict()

    if not os.path.isfile("model.sav"):
        tcp.get_train_data()
    else:
        model = joblib.load('model.sav')
        #  test data
        test_data = []
        test_data.append({"feature": "cần phải nheo mắt để nhìn thấy rõ ràng. đau đầu do quá mỏi mắt.", "target": "cận thị"})
        # test_data.append({"feature": "thường xuyên bị thiếu máu, người gầy, da xanh, niêm mạc mắt nhợt", "target": ""})
        df_test = pd.DataFrame(test_data)
        predicted = model.predict(df_test["feature"])

        # Print predicted result
        print(predicted)

        ls = model.predict_proba(df_test["feature"])
        # print(ls[0])
        print(model.score(df_test.feature, df_test.target))
        print(max(ls[0]))

        score = metrics.accuracy_score(df_test.target, predicted)
        print("accuracy:   %0.3f" % score)

        df_train = pd.read_json('sk.json', encoding="utf-8")
        print(model.score(df_train.feature, df_train.target))
