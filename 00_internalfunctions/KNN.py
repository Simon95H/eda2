import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split
class KNN:
    def __init__(self):
        pass
    # Samples aufspalten in Training, Validierung, Test
    def split_sample(self,x,y,shuffle=True,sections=(.6,.25,.15)):
        self.sections = sections
        self.shuffle = shuffle
        tmp= train_test_split(x, y, test_size=np.sum(sections[1:]),shuffle=shuffle)
        # zusätzliche Unterteilung für Testdaten
        tmp2 = train_test_split(tmp[1], tmp[3], test_size=sections[-1],shuffle=shuffle)

        # 0 = train, 1= val, 2= test
        if tmp[0].ndim ==1:
            self.x=list();self.x.append(tmp[0].reshape(-1,1));self.x.append(tmp2[0].reshape(-1,1));self.x.append(tmp2[1].reshape(-1,1))
            self.y=list();self.y.append(tmp[0].reshape(-1,1));self.y.append(tmp2[0].reshape(-1,1));self.y.append(tmp2[1].reshape(-1,1))

        else:
            self.x=list();self.x.append(tmp[0]);self.x.append(tmp2[0]);self.x.append(tmp2[1])    
            self.y=list();self.y.append(tmp[2]);self.y.append(tmp2[2]);self.y.append(tmp2[3])
    
    def scaler(self,method):
        self.scaler =method
        if self.scaler =="MinMax":
            self.scalerX = MinMaxScaler()
            self.scalerY = MinMaxScaler()
        elif self.scaler =="Standard":
            self.scalerX = StandardScaler()
            self.scalerY = StandardScaler()
        # 0 = train, 1= val, 2= test
        self.x_norm = list();
	# Fitting nur auf Trainingsdaten
        self.x_norm.append(self.scalerX.fit_transform(self.x[0]))
        [self.x_norm.append(self.scalerX.transform(self.x[i])) for i in range(1,3)]
        self.y_norm = list();self.y_norm.append(self.scalerY.fit_transform(self.y[0]));
        [self.y_norm.append(self.scalerY.fit_transform(self.y[i])) for i in range(1,3)];