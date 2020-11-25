from gameEvaluator import rule_set


methods=['centroid', 'LOM', 'MOM', 'FOM', 'bisection', 'sums']
results=[]
for m in methods:
    results.append((rule_set({'duration':4, 'difficulty':7.5}, d_method=m, a_method='Larsen'), m.upper()))

rule_set.plot(results)