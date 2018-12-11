#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.externals import joblib
import os
from sklearn import metrics

APP_ROOT = os.path.dirname(__file__)


class TextClassificationPredict(object):
    def __init__(self):
        self.test = None
        self.model = joblib.load(APP_ROOT + '/model.sav')
        self.model_conv = joblib.load((APP_ROOT + '/model_conv.sav'))
        print('Load all model success')

    def get_model(self):
        return self.model

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
        return 'Có thể bạn đang bị: {res}\nĐộ tin cậy: {per:.2f}%'.format(res=result, per=accu * 100)

    def predict_conv(self, pred_text):
        test_data = []
        test_data.append({"feature": pred_text, "target": ""})
        df_test = pd.DataFrame(test_data)
        predicted = self.model_conv.predict(df_test["feature"])

        # Print predicted result
        print(predicted)
        result = predicted[0]
        proba = self.model_conv.predict_proba(df_test["feature"])
        accu = max(proba[0])
        return result, accu


if __name__ == '__main__':
    tcp = TextClassificationPredict()

    if not os.path.isfile("model_conv.sav"):
        print("no model found")
    else:
        model = joblib.load('model_conv.sav')
        #  test data
        test_data = []
        test_data.append({"feature": "hello", "target": "chao_hoi"})
        df_test = pd.DataFrame(test_data)
        predicted = model.predict(df_test["feature"])

        # Print predicted result
        print(predicted)

        ls = model.predict_proba(df_test["feature"])
        # print(ls[0])
        print("accuracy:  %0.3f" % max(ls[0]))

        score = metrics.accuracy_score(df_test.target, predicted)
        print("accuracy:   %0.3f" % score)
