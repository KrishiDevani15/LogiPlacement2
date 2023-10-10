import numpy as np
import pickle

model = pickle.load(open('E:/apps/dashboard/Model/place_predict.pkl', 'rb'))
print(model)

data = [10,10,10,10,100,50,18,100,100,100,10,100,10,100,20]
input_data_as_numpy_array = np.array(data)
reshape = input_data_as_numpy_array.reshape(1,-1)
    # print(list(request.form.values()))
val = model.predict([data])
res = val[0]/100

print(res)
val_str = ''
if res < 50:
    res = str(res)
    val_str = "You need to prepare well!!"
    
elif res >49:
    res = str(res)
    val_str = "All the very best, you are doing well!! Your placement chances are" + res + "%"
    
else:
    val_str = "Something went wrong! Try again later."