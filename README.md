# Here is my version of Gilded Rose problem in Python 

# Purpose
This coding challenge is to go over refactoring of code, using tests to ensure the code acts the same as before the refactoring. Also to make the code more manageable and readable, for future generations of developers or yourself if you are unlucky. 

# Assumptions I took
1. Item quality cannot be less than 0 (Even when passed to the class as less than 0)
2. Item quality cannot be more than 50 (Even when passed to the class as more than 50)
3. Sulfuras is always 80 

These assumptions are a little different to the original code. I would say that the requirements file is more valid for the approach than the existing code. Care would have to be taken rolling this out, as the outputs are slightly different. Picking up errors need to be handled on code refactoring not just making sure the new outputs match the existing outputs 100%. 

# Approach I took
1. Write tests on the existing code (I aligned the test with the requirements sheet)
2. Run tests on existing code to make sure it works
3. Tests failed, as the outputs do not match the requirements sheet (I made the assumption that it was the source of truth)
4. Refactor the code to make it more readable, reliable and improve the formatting
5. Rerun the tests to ensure that the new code works as intended