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
    print y_target
    x_feature = mydata[:, 2:]

    print x_feature
    #print y_target

    regr = MLPRegressor(hidden_layer_sizes=(4,6, 5))

    regr.fit(x_feature[:-50], y_target[:-50])
    print "predict",regr.predict(x_feature[-50:])
    print y_target[-50:]
    print regr.score(x_feature[-50:], y_target[-50:])
