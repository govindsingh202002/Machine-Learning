## this method use scikit-learn resample library which retake same data points at the same place for upsampling
#### means no-variance in data

# import pandas as pd
# import numpy as np
# np.random.seed(0)
# import seaborn as sns
# import matplotlib.pyplot as plt
# total_sample=1000
# class_0_size=int(total_sample*0.9) # 90%
# class_1_size=total_sample-class_0_size

# # create dataframes with 3-4 features including target colum in which 0 for class 0 and 1 for class 1
# #loc=mean and scale=standard deviation

# class_0=pd.DataFrame({
#     'x1':np.random.normal(loc=0,scale=1,size=class_0_size),
#     'x2':np.random.normal(loc=4,scale=4,size=class_0_size),
#     'target':[0]*class_0_size
# })

# class_1=pd.DataFrame({
#     'x1':np.random.normal(loc=0,scale=1,size=class_1_size),
#     'x2':np.random.normal(loc=4,scale=4,size=class_1_size),
#     'target':[1]*class_1_size
# })

# df=pd.concat([class_0,class_1]).reset_index(drop=True)

# df_minority=df[df['target']==1]
# df_majority=df[df['target']==0]
# # print(df_minority.shape,df_majority.shape)

# # sns.scatterplot(df,x='x1',y='x2',hue='target')
# # plt.show()

# from sklearn.utils import resample
# df_upsampled=resample(df_minority,replace=True,n_samples=len(df_majority),random_state=1)
# # print(df_upsampled.shape)

# upsampled_balanced_df=pd.concat([df_majority,df_upsampled]).reset_index(drop=True)

# sns.scatterplot(upsampled_balanced_df,x='x1',y='x2',hue='target')
# plt.show()


## This is SMOTE(synthetic minority oversampling technique):- 
### it connect two nearest data point and create new data points on that line resultant getting new data points with variance
from sklearn.datasets import make_classification
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

X,y=make_classification(n_samples=1000, n_features=2, n_informative=2, n_redundant=0, n_repeated=0, n_classes=2, n_clusters_per_class=1, weights=[0.9], flip_y=0.01, class_sep=1.0, hypercube=True, shift=0.0, scale=1.0, shuffle=True, random_state=None, return_X_y=True)

# print(X.shape)
df=pd.concat([pd.DataFrame(X,columns=['x1','x2']),pd.DataFrame(y,columns=['target'])],axis=1).reset_index(drop=True)
# print(df.head())

# sns.scatterplot(df,x='x1',y='x2',hue='target')
# plt.show()
from imblearn.over_sampling import SMOTE
oversample=SMOTE()
X,y=oversample.fit_resample(df[['x1','x2']],df[['target']])
df1=pd.concat([pd.DataFrame(X,columns=['x1','x2']),pd.DataFrame(y,columns=['target'])],axis=1).reset_index(drop=True)
# print(df.head())

sns.scatterplot(df1,x='x1',y='x2',hue='target')
plt.show()