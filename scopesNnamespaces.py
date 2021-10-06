a = 0 # Global Variable
def change_global_scope_directly(): 
  # -------------Wrong Way------------
  a = 1 # Local variable a is created and changing this won't change Global value
  print("Direct Local Print a: ",a)
change_global_scope_directly()
print("Direct Global Print a: ",a)

# to avoid above problem we Use Global keyword
def change_global_scope_with_global_keyword():
  # ---------Correct Way---------------
  global a # Global variable is referred instead of creating new local value
  a = 2
  print("using global Local Print a: ", a)
change_global_scope_with_global_keyword()
print("using global, global print a: ",a)

print("____________________________________________/n")

# similarly when a variable is created in one function, then it is created in that function scope only

# in the example lets try changing b defined in outer_function  inside inner_function

def outer_function(): 
  b = "apple" # Created in function one so it has scope only in outer function
  def changing_outerfunction_var_using_global_keyword():
    # -------------Wrong Way------------
    global b # here now it wont refer the outer_function variable b, but creates a new global variable b.
    b="butterfly" 
    print("inside inner function b: ",b)
  changing_outerfunction_var_using_global_keyword()
  print("inside outer function b: ",b)
outer_function()
print("globally b: ",b)

def outer_function_again(): 
  c = "cardboard" # Created in function one so it has scope only in outer function
  def changing_outerfunction_var_using_nonlocal_keyword():
    # -------------Correct Way------------
    nonlocal c # here it refers the outer_function variable b.
    c="dock" 
    print("inside inner function c: ",c)
  changing_outerfunction_var_using_nonlocal_keyword()
  print("inside outer function c: ",c)
outer_function_again()



print("____________________________________________/n")