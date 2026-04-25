from fractions import Fraction

def interlacing_fib_sequences(j, r):
    """
    Given whether it is \mathscr{F}_{r}^{(2, 1)} or \mathscr{F}_{r}^{(2, 2)} (j=1 or j=2), generates the rth term of the 
    interlacing fibonacci sequence with recurrence relation given by F_r = - F_1 - (1 / 5) * F_0.
    """
    if j == 1:
        F_0 = 2
        F_1 = -1
    if j == 2:
        F_0 = 1
        F_1 = -1
    if r == 0:
        return F_0
    if r == 1:
        return F_1
    for i in range(2, r + 1):
        F_r = - F_1 - (1 / 5) * F_0
        F_0 = F_1
        F_1 = F_r
    return F_r

def first_r_terms_sequence_powers(j, r, n):
    """
    Given whether it is \mathscr{F}_{r}^{(2, 1)} or \mathscr{F}_{r}^{(2, 2)} (j=1 or j=2), generates the first r terms of the 
    interlacing fibonacci sequence taken to a given power, n.
    """
    sequence = []
    for i in range(r):
        F_r = interlacing_fib_sequences(j, i) ** n
        sequence.append(F_r)
    return sequence

def first_r_terms_absolute_value_sequence(j, r):
    """
    Given whether it is \mathscr{F}_{r}^{(2, 1)} or \mathscr{F}_{r}^{(2, 2)} (j=1 or j=2), generates the first r terms of the 
    absolute values of the interlacing fibonacci sequence.
    """
    sequence = []
    for i in range(r):
        F_r = abs(interlacing_fib_sequences(j, i))
        sequence.append(F_r)
    return sequence

def interlacing_fib_sequences2(F_0, F_1, F_2, r):
    """
    Given the initial values F_0, F_1 and F_2, generates the rth term of the sequence with recurrence relation the same as the 
    3 dimension interlacing fib sequence.
    """
    if r == 0:
        return F_0
    if r == 1:
        return F_1
    if r == 2:
        return F_2
    for i in range(3, r + 1):
        F_r = - 2 * F_2 - F_1 - (1 / 7) * F_0
        F_0 = F_1
        F_1 = F_2
        F_2 = F_r
    return F_r

def first_r_terms_sequence2(F_0, F_1, F_2, r):
    """
    Given the initial values F_0, F_1 and F_2, generates the first r terms of the 3 dimension interlacing fib sequence.
    """
    sequence = []
    for i in range(r):
        F_r = interlacing_fib_sequences2(F_0, F_1, F_2, i)
        sequence.append(F_r)
    return sequence

def sums_of_powers(j, n):
    """
    Given whether it is the \mathscr{F}_{r}^{(2, 1)} or \mathscr{F}_{r}^{(2, 2)} sequence (j=1 or j=2), and the power of r, 
    calculates the sum to infinity of (\mathscr{F}_{r}^{(2, j)}) ** n via the formula.
    """
    if j == 1:
        if n % 2 == 1:
            summation = sum(((scipy.special.comb(n, k)) * (2 - (5) ** (- k) * interlacing_fib_sequences(1, (n - 2 * k))) / (1 + (5) ** (- n) - (5) ** (- k) * interlacing_fib_sequences(1, (n - 2 * k)))) for k in range(0, int(((n - 1) / 2) + 1)) if n % 2 == 1)
        if n % 2 == 0:
            summation = scipy.special.comb(n, n / 2) * (1) / (1 - (5) ** (- n / 2)) + sum(((scipy.special.comb(n, k)) * (2 - (5) ** (- k) * interlacing_fib_sequences(1, (n - 2 * k))) / (1 + (5) ** (- n) - (5) ** (- k) * interlacing_fib_sequences(1, (n - 2 * k)))) for k in range(0, int(n / 2)))
    if j == 2:
        if n % 2 == 1:
            summation = math.sqrt(5) ** n * sum((((scipy.special.comb(n, k)) * (-5) ** (-k) * (1 / math.sqrt(5)) * interlacing_fib_sequences(2, n - 1 - 2 * k)) / (1 + 5 ** (-n) - 5 ** (-k) * interlacing_fib_sequences(1, n - 2 * k))) for k in range(0, int(((n - 1) / 2) + 1)))
        if n % 2 == 0:
            summation = math.sqrt(5) ** n * (scipy.special.comb(n, n / 2) * ((- 1) ** (n / 2)) * (5) ** (- n / 2) / (1 - (5) ** (- n / 2)) + sum((((scipy.special.comb(n, k)) * ((- 5) ** (- k) * interlacing_fib_sequences(1, n - 2 * k) - (- 1) ** k * 2 * (5) ** (- n))) / (1 + 5 ** (- n) - 5 ** (- k) * interlacing_fib_sequences(1, n - 2 * k))) for k in range(0, int(n / 2))))
    return summation
