import numpy as np
import statsmodels.api as sm

#OUTPUT
y = [1,2,3,4,3,4,5,4,5,5,4,5,4,5,4,5,6,5,4,5,4,3,4]

#INPUTS
x = [
	[4,2,3,4,5,4,5,6,7,4,8,9,8,8,6,6,5,5,5,5,5,5,5],
	[4,1,2,3,4,5,6,7,5,8,7,8,7,8,7,8,7,7,7,7,7,6,5],
	[4,1,2,5,6,7,8,9,7,8,7,8,7,7,7,7,7,7,6,6,4,4,4]
	]

def reg_m():
    ones = np.ones(len(x[0]))
    X = sm.add_constant(np.column_stack((x[0], ones)))
    for ele in x[1:]:
        X = sm.add_constant(np.column_stack((ele, X)))
    results = sm.OLS(y, X).fit()
    return results

def show_summary():
	print reg_m().summary()

#TODO: Implement the same above with the below 

# from sklearn import linear_model
# clf = linear_model.LinearRegression()
# clf.fit([[getattr(t, 'x%d' % i) for i in range(1, 8)] for t in texts],
#        [t.y for t in texts])