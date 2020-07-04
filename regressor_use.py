import numpy as np
import sys
from keras.models import load_model

pss_min = np.array([1.0, 1.0, 1.0, 1.0, 0.0, 0.7333, 0.0, 0.0, 0.1818, 0.0, 0.0, -259.78, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5455, 0.0, 0.0496, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1429, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1111, 0.0, 0.0, 0.0213, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
pss_max = np.array([70.0, 70.0, 70.0, 9.3501, 1.0, 28.1429, 70.0, 0.5, 1.0, 0.5, 250.0, 162.205, 1.0, 1.0, 1.0, 0.6667, 1.0, 6492.9972, 1.0, 7.1765, 4.0, 1.0, 1.0, 6.0985, 1.0, 17.0, 0.5, 1.0, 2.0, 1.0, 3.0, 19.5753, 0.5, 1.0, 0.5, 0.5, 0.0909, 1.0, 0.5, 0.5, 11.0, 14.0, 5.0, 0.5, 19.0, 1.0, 1.0, 1.0, 1.0, 1.0, 994512.0, 2.0, 1.0, 3.6141, 1.0, 0.5, 1.0, 1.0, 0.1429, 5.9759, 6.0, 1.0, 0.6667, 1.0, 1.0, 0.25, 1.0, 7.0, 7.7818, 56.0, 0.6, 1.6517, 20.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 0.2, 14.0, 1.0, 0.5, 1.0, 0.5, 1.0, 0.6667, 0.3333, 1.0, 1.2935, 1.0, 5.7876, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 5.0, 0.5, 2.0, 1.5827, 0.5, 6.0, 1.0, 1.0, 0.25, 1.0, 1.0, 1.0, 41.0, 1.0, 1.0, 0.25, 8720796.5455, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 6.0, 10.0, 3.0, 1.0, 1.0, 39.0, 44.0, 1.0, 0.5, 1.0, 1.5, 39.0, 27.5, 0.8571, 0.5, 0.5, 1.0, 0.5, 12.0, 1.0, 1.0, 1.0, 1.0, 1.0, 20.0, 0.3333])

pipeline_pss = load_model("models/model_regressor_v2_10.h5")

raw_input = str(sys.argv[1])
feats = raw_input.split(",")
x = []
for f in feats:
    x.append(float(f))
X = np.array(x)

X_norm = (X - pss_min) / (pss_max - pss_min)

prediction = pipeline_pss.predict(np.array([X_norm]))

result = round(prediction[0][0], 2)

if result < 0.01:
    result = 0.01
if result > 1:
    result = 1.0

print("result:",result)

