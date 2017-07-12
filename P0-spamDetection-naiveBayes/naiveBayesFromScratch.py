"""
Naive Bayes' is an extension of Bayes' theorem that assumes that all the features are independent of each other.
                                        P(y) * P(x1, x2, ..., xn | y)
Naive Bayes: P(y | x1, x2, ..., xn) = --------------------------------
                                            P(x1, x2, ..., xn)

Exercise:
Prob of Jill Stein gives a speech: 0.5 -----------> P(J)
Prob that Jill Stein says 'freedom': 0.1 ---------> P(F|J)
Prob that Jill Stein says 'immigration': 0.1 -----> P(I|J)
Prob that Jill Stein says 'environment': 0.8 -----> P(E|J)
Prob of Gary Johnson gives a speech: 0.5 ---------> P(J)
Prob that Gary Johnson says 'freedom': 0.7 -------> P(F|G)
Prob that Gary Johnson says 'immigration': 0.2 ---> P(I|G)
Prob that Gary Johnson says 'environment': 0.1 ---> P(E|G)
-> Find prob each say Freedom and Immigration
-> Find P(J|F,I), P(G|F,I)
"""

# P(J)
p_j = 0.5

# P(F/J)
p_j_f = 0.1

# P(I/J)
p_j_i = 0.1

p_j_text = p_j * p_j_f * p_j_i


# P(G)
p_g = 0.5

# P(F/G)
p_g_f = 0.7

# P(I/G)
p_g_i = 0.2

p_g_text = p_g * p_g_f * p_g_i


# P(F,I)
p_f_i = p_j_text + p_g_text
print 'Probability of words freedom and immigration being said are:',\
    format(p_f_i)


# P(J|F,I) = (P(J) * P(F|J) * P(I|J)) / P(F,I)
p_j_fi = p_j_text / p_f_i
print 'The probability of Jill Stein saying the words Freedom and Immigration:',\
    format(p_j_fi)

p_g_fi = p_g_text / p_f_i
print 'The probability of Gary Johnson saying the words Freedom and Immigration:',\
    format(p_g_fi)
