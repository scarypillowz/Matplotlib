import csv
import numpy as np

def bop_data_reader():
    with open('./datasets/BrentOilPrices.csv') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
    
        dataset = list()
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        months_dic = {months[m_idx]: m_idx + 1 for m_idx in range(len(months))}
    
        for data in csvreader:        
            price = data[-1]
            date = data[0]
            try:
                D, M, Y = date.split('-')
                if int(Y) >= 87:
                    M = months_dic[M]
                    dataset.append([Y, M, D, price])
            except:
                pass
    
    dataset = np.array(dataset).astype(float)
    return dataset

# 특정 연도의 데이터만 추출하기
def get_tyear_data(dataset, t_year):
    t_idx = np.where(dataset[:, 0] == t_year)
    t_data = dataset[t_idx]
    return t_data