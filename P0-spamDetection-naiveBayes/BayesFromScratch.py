"""
                         P(B|A) * P(A)
Bayes formula: P(A|B) = ---------------
                              P(B)

Exercise:
P(D) = prob of having diabetes
P(Pos) = prob of getting positive test result
P(Neg) = prob of getting negative test result
P(Pos|D) = prob of getting pos test result, given patient has diabetes
P(Neg|~D) = prob of getting neg test result, given patient has no diabetes
-> Find P(D|Pos), P(~D|Pos)
"""

# P(D)
p_diabetes = 0.01

# P(~D)
p_no_diabetes = 0.99

# Sensitivity or P(Pos|D)
p_pos_diabetes = 0.9

# Specificity or P(Neg/~D)
p_neg_no_diabetes = 0.9

# P(Pos)
p_pos = (p_diabetes * p_pos_diabetes) + (p_no_diabetes * (1 - p_neg_no_diabetes))
print('The probability of getting a positive test result P(Pos) is: {}',
      format(p_pos))

# P(D|Pos)
p_diabetes_pos = (p_diabetes * p_pos_diabetes) / p_pos
print('Probability of an individual having diabetes, ',
      'given that that individual got a positive test result is:',
      format(p_diabetes_pos))

# P(Pos/~D) = 1 - P(Neg/~D)
p_pos_no_diabetes = 0.1

# P(~D|Pos)
p_no_diabetes_pos = (p_no_diabetes * p_pos_no_diabetes) / p_pos
print 'Probability of an individual not having diabetes,',\
    'given that that individual got a positive test result is:',\
    p_no_diabetes_pos