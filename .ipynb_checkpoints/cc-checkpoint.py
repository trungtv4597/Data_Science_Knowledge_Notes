import scipy.stats as sta
from math import sqrt


def t_score(confidence, n, n_side):
    return sta.t.ppf((confidence/n_side), n-1)
        
    
def t_test(xbar, h0, standard_error):
    return ((xbar - h0) / standard_error)


def decision_the_null(Xbar, h0, standard_error, confidence, n, n_side):
    T = t_test(Xbar, h0, standard_error)
    t = t_score(confidence, n, n_side)
    
    print('T-test:', round(T))
    print('t-score:', round(t))
    
    if abs(T) > abs(t):
        print('Decision: REJECT the null hypothesis with level of confidence {}%'.format(confidence*100))
    else:
        print('Decision: ACCEPT the null hypothesis with level of confidence {}%'.format(confidence*100))

        
def t_score_2_indep_samples(confidence, n_x, n_y, n_side):
    return sta.t.ppf((confidence/n_side), n_x + n_y - 2)


def t_test_2_indep_sample(xbar, ybar, h0, x_var, y_var, n_x, n_y):
    std_pool = ((n_x-1)*x_var + (n_y-1)*y_var) / (n_x + n_y - 2)
    return ((xbar - ybar) - h0) / sqrt((std_pool/n_x)+(std_pool/n_y))


def decision_the_null_2_indep_sample(xbar, ybar, h0, x_var, y_var, confidence, n_x, n_y, n_side):
    T = t_test_2_indep_sample(xbar, ybar, h0, x_var, y_var, n_x, n_y)
    t = t_score_2_indep_samples(confidence, n_x, n_y, n_side)
    
    print('Test statistics:', round(T))
    print('Critical value:', round(t))
    
    if abs(T) > abs(t):
        print('Decision: REJECT the null hypothesis with level of confidence {}%'.format(confidence*100))
    else:
        print('Decision: ACCEPT the null hypothesis with level of confidence {}%'.format(confidence*100))



if __name__ == '__main__':
    x = critical_value(confidence=.95, n=11, n_side=2)
    print(x)