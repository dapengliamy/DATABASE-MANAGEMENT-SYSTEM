from sklearn import linear_model
import numpy as np
from sklearn.preprocessing import StandardScaler
import sys
import random
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
import numpy as np

if __name__ == "__main__":
    data = []
    for i, line in enumerate(open("workfile.csv")):
        if i == 0:
            continue
        fields = line.strip().split(",")
        data.append(map(float, fields))
        

    mydata = np.array(data)
        
    y_target = mydata[:, 1]
    x_feature = mydata[:, 2:]

    x_train = x_feature[:-50]
    x_test = x_feature[-50:]

    scaler = StandardScaler()
    scaler.fit(x_train)
    x_train = scaler.transform(x_train)
    x_test = scaler.transform(x_test)

   # print x_feature
   # print y_target

    regr = linear_model.LinearRegression()
    
    regr.fit(x_train, y_target[:-50])
    print (regr.coef_)
    #print np.mean((regr.predict(x_test)-y_target[-30:])**2)
    predict_data = regr.predict(x_test)
    f = open('predict.csv', 'w+')
    for i in predict_data:
        f.write(str(i))
        f.write("\n")
        
    print "y_target", y_target[-50:]
    print regr.score(x_test, y_target[-50:])
    
    regrNeural = MLPRegressor(hidden_layer_sizes=(4,6, 5))
    regrNeural.fit(x_feature[:-50], y_target[:-50])
    predict_data = regrNeural.predict(x_feature[-50:])
    f = open('predict_neuron.csv','w+')
    for i in predict_data:
        f.write(str(i))
        f.write("\n")
    print regrNeural.score(x_feature[-50:], y_target[-50:])
    
    
