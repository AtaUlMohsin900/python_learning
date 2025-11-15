# String & Numeric Values can operate together with *
A, B = 2,3
Txt = "a"
result = 2*Txt *3
print(f"{result} Number of 'a' printed in : {len(result)} times")  


# String & Numeric can operate with = + (Concatenate).
A, B = "2", 3
txt = "s"
print((A+txt)*B)  # precedence(A+txt) then *B


# Numeric Value can operate with all arithmetic operators.
A, B = 2, 3
c = 4
print(A + B* c)   # precedence(B*c) then +A


  # Arithmetic expression with integer and Float with result in Float.
A, B = 10, 5.0
c = A * B
print(c)

# Result of division operator with two integer will be Float.
A, B = 1,2
C = A/B 
print(c)

# integer division with Float and integer will give integer display as Flout

A, B = 1.5, 3
c = A//B
print(C, A/B)

# Floor gives lessor than or equal to the Float value
# Result of (A//B) is same as floor (A/B)

A, B = 12, 5
c = A//B
print(c)