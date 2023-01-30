def fit(evals , Y):
    n = len(evals)
    sum=0
    for i in range(n):
        sum+=(evals[i]-Y[i])**2
    return sum/n    