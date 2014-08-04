#adults dataset
def load_adult():
    """loads adult dataset"""
    remove_sp = lambda n: n.replace(' ', '')
    last_column = lambda i: i.pop(-1)
    binary_= lambda u: 0 if  u == '<=50K' else 1
    
    defs_ = [
      {'age': None},
      {'workclass': ['Private', '?', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov', 'Local-gov', 'State-gov', 'Without-pay', 'Never-worked']},
      {'fnlwgt': None},
      {'education': ['Bachelors', '?', ' Some-college', ' 11th', ' HS-grad', ' Prof-school', ' Assoc-acdm', ' Assoc-voc', ' 9th', ' 7th-8th', ' 12th', ' Masters', ' 1st-4th', ' 10th', ' Doctorate', ' 5th-6th', ' Preschool']},
      {'education-num': None},
      {'marital-status': ['Married-civ-spouse', '?', 'Divorced', 'Never-married', 'Separated', 'Widowed', ' Married-spouse-absent', ' Married-AF-spouse']},
      {'occupation': ['Tech-support', ' Craft-repair', '?', ' Other-service', ' Sales', ' Exec-managerial', ' Prof-specialty', ' Handlers-cleaners', ' Machine-op-inspct', 'Adm-clerical', ' Farming-fishing', ' Transport-moving', ' Priv-house-serv', ' Protective-serv', ' Armed-Forces']},
      {'relationship': ['Wife', ' Own-child', ' Husband', '?', ' Not-in-family', ' Other-relative', ' Unmarried']},
      {'race': ['White', ' Asian-Pac-Islander', '?', ' Amer-Indian-Eskimo', ' Other', ' Black']},
      {'sex': ['Female', ' Male', '?']},
      {'capital-gain': None},
      {'capital-loss': None},
      {'hours-per-week': None},
      {'native-country': ['United-States', '?', ' Cambodia', ' England', ' Puerto-Rico', ' Canada', ' Germany', ' Outlying-US(Guam-USVI-etc)', ' India', ' Japan', ' Greece', ' South', ' China', ' Cuba', ' Iran', ' Honduras', ' Philippines', ' Italy', ' Poland', ' Jamaica', ' Vietnam', ' Mexico', ' Portugal', ' Ireland', ' France', ' Dominican-Republic', ' Laos', ' Ecuador', ' Taiwan', ' Haiti', ' Columbia', ' Hungary', ' Guatemala', ' Nicaragua', ' Scotland', ' Thailand', ' Yugoslavia', ' El-Salvador', ' Trinadad&Tobago', ' Peru', ' Hong', ' Holand-Netherlands']}
    ]
    v =-1
    
    for i,a in enumerate(defs_):
        current_col = a
        v += 1
        key_ = current_col.keys()[0]
        if current_col[key_]:
            defs_[i][key_] = dict([(b.strip(' '), i_) for b, i_ in zip(current_col[key_], range(0, len(current_col[key_])))])
        defs_[i][v] = defs_[i].pop(key_)
    
    y = ''
    f  = open("datasets_/adults.txt", 'rb')
    for a in f:
       y += a
    y = y.split('\n')
    y.pop(-1)
    labels_ = []
    for n, j in enumerate(y):
        y[n] = y[n].split(',')
        current_ = map(remove_sp, y[n])
        indicator_ = current_.pop(-1)
        labels_.append(indicator_)
        for i, a in enumerate(current_):
            column_ = defs_[i]
            if column_.values()[0] == None:
                current_[i]  = float(current_[i])
            elif column_.values()[0].has_key(current_[i]):
                current_[i] = column_.values()[0][current_[i]]
        y[n]  = current_
    
    return y, map(binary_, labels_)                       

#wines dataset
def load_wines():
    y = ''
    f = open('datasets_/wines.txt', 'rb')
    for a in f:
        y += a
    y = y.split('\n')
    labels_ = []
    for i, a in enumerate(y):
        y[i] = y[i].split(',')
        indicator_ = y[i].pop(0)
        labels_.append(indicator_)
        y[i] = map(float, y[i])
    return y, map(float, labels_)

#car dataset
#http://archive.ics.uci.edu/ml/machine-learning-databases/car/
def load_cars():
    def replace_stuff(n):
        if n in ['more','5more']:
            return 5
        else:
            return n
    
    defs_ = [
                 {'buying': {'vhigh': 4, 'high': 3, 'med': 2, 'low': 1}},
                 {'maint': {'vhigh': 4, 'high': 3, 'med': 2, 'low': 1}},
                 {'doors': None},
                 {'persons': None},
                 {'lug_boot': {'small': 1, 'med': 2, 'big': 3}},
                 {'safety': {'low': 1, 'med': 2, 'high': 3}},
                 ]
    v = -1
    for i, a in enumerate(defs_):
        v += 1
        key_ = defs_[i].keys()[0]
        defs_[i][v] = defs_[i].pop(key_)
    
    y = ''
    f = open('datasets_/cars.txt', 'rb')
    for a in f:
        y += a
    y = y.split('\n')
    labels_ = []
    for i, a in enumerate(y):
        y[i] = y[i].split(',')
        indicator_ = y[i].pop(-1)
        labels_.append(indicator_)
        current_ = map(replace_stuff, y[i])
        for j, b in enumerate(current_):
            col_ = defs_[j]
            item_ = current_[j]
            if col_.values()[0] == None:
                current_[j]= float(current_[j])
            else:
                if col_.values()[0].has_key(current_[j]):
                    current_[j] = col_.values()[0][current_[j]]
        y[i] = current_
    return y, labels_

#yeasts dataset (all continuous)
#http://archive.ics.uci.edu/ml/machine-learning-databases/yeast/yeast.data
def load_yeast():
    defs_ = {'sequence_name': str,
                 'mcg': float,
                 'gvh': float,
                 'alm': float,
                 'mit': float,
                 'erl': float,
                 'pox': float,
                 'vac': float,
                 'nuc': float,
                 'class': str
    }

    f = open('datasets_/yeast.txt', 'rb')
    y = ''
    for a in f:
        y += a
    y = y.split('\n')
    labels_ = []

    for i, a in enumerate(y):
        y[i]= y[i].split(' ')
        indicator_ = y[i].pop(-1)
        labels_.append(indicator_)
        remove_first = y[i].pop(0)
        y[i] = map(float, filter(lambda n: len(n) > 0, y[i]))

    return y, labels_

#wine quality dataset (all continuous)
#http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality.names
def load_wine_quality():
    defs_ = {
        'fixed acidity': float,
        'volatile acidity': float,
        'citric acid': float,
        'residual sugar': float,
        'chlorides': float,
        'free sulfur dioxide': float,
        'total sulfur dioxide': float,
        'density': float,
        'pH': float,
        'sulphates': float,
        'alcohol': float,
        'quality': int
        }
    
    f = open('datasets_/wine_quality.txt', 'rb')
    y = ''
    for a in f:
        y +=  a

    y = y.split('\n')
    y.pop(-1)
    labels_ = []
    for i, a in enumerate(y):
        y[i] = filter(lambda n : len(n) > 0, y[i].split('\t'))
        
        indicator_ = y[i].pop(-1)
        labels_.append(int(indicator_))
        y[i] = map(float, y[i])
        
    return y, labels_
    
    
#seeds dataset (all continuous)
#https://archive.ics.uci.edu/ml/machine-learning-databases/00236/seeds_dataset.txt
def load_seeds():
    defs_ = {
        'area': float,
        'perimeter': float,
        'compactness': float,
        'width of kernel': float,
        'asymmetry coefficient': float,
        'length of kernel groove': float,
        'seed type': int
        }
    f = open('datasets_/seeds.txt', 'rb')
    y = ''
    for a in f:
        y += a
    y = y.split('\n')
    labels_ = []
    for i, a in enumerate(y):
        y[i] = filter(lambda n: len(n) > 0, y[i].split('\t'))
        indicator_ = y[i].pop(-1)
        labels_.append(int(indicator_))
        y[i] = map(float, y[i])
    return y, labels_
            
        
        

    



        
    
                    
                
            
    
    

    
    
    
