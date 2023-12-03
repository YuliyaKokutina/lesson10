import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(pd.get_dummies(data).replace({ True : 1 , False : 0 }))