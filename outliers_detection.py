from sklearn.datasets import load_digits
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data=load_digits()
df_X=pd.DataFrame(data.data,columns=data.feature_names)
df_y=pd.DataFrame(data.target,columns=['target'])
df=pd.concat([df_X,df_y],axis=1).reset_index(drop=True)
X=list(df['pixel_0_3'])
minimum,Q1,median,Q3,maximum=np.quantile(X,[0.00,0.25,0.50,0.75,1.00])
IQR=Q3-Q1
lower_fence=Q1-1.5*(IQR)
higher_fence=Q3+1.5*(IQR)
# print(minimum,Q1,median,Q3,maximum,lower_fence,higher_fence)
outliers=[outlier for outlier in X if outlier<lower_fence or outlier>higher_fence]
# sns.boxplot(X)
# plt.show()
print(outliers)