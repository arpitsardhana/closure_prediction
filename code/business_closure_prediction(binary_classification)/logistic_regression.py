import pandas as pd
import statsmodels.api as sm
import pylab as pl
import numpy as np

def cartesian(arrays, out=None):
    """
    Generate a cartesian product of input arrays.
    Parameters
    ----------
    arrays : list of array-like
        1-D arrays to form the cartesian product of.
    out : ndarray
        Array to place the cartesian product in.
    Returns
    -------
    out : ndarray
        2-D array of shape (M, len(arrays)) containing cartesian products
        formed of input arrays.
    Examples
    --------
    >>> cartesian(([1, 2, 3], [4, 5], [6, 7]))
    array([[1, 4, 6],
           [1, 4, 7],
           [1, 5, 6],
           [1, 5, 7],
           [2, 4, 6],
           [2, 4, 7],
           [2, 5, 6],
           [2, 5, 7],
           [3, 4, 6],
           [3, 4, 7],
           [3, 5, 6],
           [3, 5, 7]])
    """

    arrays = [np.asarray(x) for x in arrays]
    dtype = arrays[0].dtype

    n = np.prod([x.size for x in arrays])
    if out is None:
        out = np.zeros([n, len(arrays)], dtype=dtype)

    m = n / arrays[0].size
    out[:,0] = np.repeat(arrays[0], m)
    if arrays[1:]:
        cartesian(arrays[1:], out=out[0:m,1:])
        for j in xrange(1, arrays[0].size):
            out[j*m:(j+1)*m,1:] = out[0:m,1:]
    return out

df = pd.read_csv("logisticreg.csv")

print df.describe()
#print df.head()

#print df.columns

#print df.std()
#print pd.crosstab(df['closed'],df['noise'],rownames=['closed'])
#print pd.crosstab(df['closed'],df['price'],rownames=['closed'])
#print pd.crosstab(df['closed'],df['stars'],rownames=['closed'])

#df.hist()
#pl.show()

dummy_price = pd.get_dummies(df['price'],prefix='price')
#print dummy_price.head()

#cols_to_keep = ['closed','reviews','stars']
cols_to_keep = ['closed','reviews','stars','noise']

data = df[cols_to_keep].join(dummy_price.ix[:,'price_1':])
#print data.head()

data['intercept'] = 1.0

train_cols = data.columns[1:]

logit = sm.Logit(data['closed'],data[train_cols])

result = logit.fit()

#print result.summary()

#print result.conf_int()

#print np.exp(result.params)

params = result.params
conf = result.conf_int()
conf['OR'] = params
conf.colums = ['2.5%','97.5%','OR']
#print np.exp(conf)

review_v = np.linspace(data['reviews'].min(),data['reviews'].max(),10)

stars_v  = np.linspace(data['stars'].min(),data['stars'].max(),5)
noise_v  = np.linspace(data['noise'].min(),data['noise'].max(),4)
#good     = np.linspace(data['goodcount'].min(),data['goodcount'].max(),7)
#park     = np.linspace(data['parking'].min(),data['parking'].max(),2)
#ambience     = np.linspace(data['ambience'].min(),data['ambience'].max(),2)
#lunch     = np.linspace(data['lunch'].min(),data['lunch'].max(),2)
#group     = np.linspace(data['group'].min(),data['group'].max(),2)
#dinner     = np.linspace(data['dinner'].min(),data['dinner'].max(),2)
#prices     = np.linspace(data['price'].min(),data['price'].max(),4)
combos = pd.DataFrame(cartesian([review_v,stars_v,noise_v,[1,2,3,4,5],[1.]]))
#combos = pd.DataFrame(cartesian([[1,2,3,4,5],[1.]]))
combos.columns = ['reviews','stars','noise','price','intercept']

dummy_price = pd.get_dummies(df['price'],prefix='price')
dummy_price.columns = ['price_0','price_1','price_2','price_3','price_4']

#print dummy_price.head()

cols_to_keep = ['reviews','stars','noise','price','intercept']

combos = combos[cols_to_keep].join(dummy_price.ix[:,'price_1':])

combos['closed_pred'] = result.predict(combos[train_cols])

#print combos.head()

def isolate_and_plot(variable):
    # isolate gre and class rank
    grouped = pd.pivot_table(combos, values=['closed_pred'], rows=[variable,'price'], aggfunc=np.mean)
    
    # in case you're curious as to what this looks like
    # print grouped.head()
    #                      admit_pred
    # gre        prestige            
    # 220.000000 1           0.282462
    #            2           0.169987
    #            3           0.096544
    #            4           0.079859
    # 284.444444 1           0.311718
    
    # make a plot
    colors = 'rbgyrbgy'
    for col in combos.price.unique():
        plt_data = grouped.ix[grouped.index.get_level_values(1)==col]
        pl.plot(plt_data.index.get_level_values(0), plt_data['closed_pred'],
                color=colors[int(col)])

    pl.xlabel(variable)
    pl.ylabel("P(closed=1)")
    pl.legend(['1', '2', '3', '4'], loc='upper left', title='Price')
    pl.title("Prob(Closed=1) isolating " + variable + " and price")
    pl.show()

isolate_and_plot('reviews')
isolate_and_plot('noise')
isolate_and_plot('stars')
#isolate_and_plot('goodcount')
#isolate_and_plot('parking')
