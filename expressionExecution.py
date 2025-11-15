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