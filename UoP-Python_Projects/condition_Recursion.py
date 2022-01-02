#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CATHERINE O. ACHIENG
#
# Created:     24/09/2021
# Copyright:   (c) CATHERINE O. ACHIENG 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------


# Chained and nested conditionals are talking about flow controls. Let's learn the difference between:

# * Chained conditional *

# Here we use if/elif/else flow controls and they are on the same level/intended to same depth.
# It means, we don't have nested conditionals inside the main flow controls.
# To have it more clear, let's have a look on the following example:

a = 10
b = 15

if a > b:
    print("A is bigger than b")
elif a < b:
    print("B is bigger than A")
else:
    print("A and B are equalised ")

#  * Nested conditional *

# It goes here on using flow controls inside others. Let's walk through the next example to have it clear.

import datetime

current_hour = int(datetime.datetime.now().strftime("%H"))

if 12 > current_hour >= 0:
    print("Good Morning!")
elif 12 <= current_hour < 20:
    if 12 < current_hour < 17:
        print("Good afternoon!")
    else:
        print("Good evening!")
else:
    print("Good night!")

# In the above example, I used datetime class to get the current hour and then I casted it to integer.
# I went through different possibilities using flow controls, to print the right greeting depending on the current time. If you
# have a look at 'elif', you can see that there's a deeper if/else. In that case, it's called nested conditional.

# ***********************

# If you can't understand easily the nested conditionals, you can then do following
# Don't use nested conditionals and replace it with elif
# Let's demonstrate it using the previous example

if 12 > current_hour >= 0:
    print("Good Morning!")
elif 12 <= current_hour < 17:
    print("Good afternoon!")
elif 17 <= current_hour < 20:
    print("Good evening!")
else:
    print("Good night!")

# Surly, the output is still the same. I replaced 'elif' and its nested conditionals with elif. Now we can read through easily.
