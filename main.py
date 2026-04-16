# Create a welcome message.
# Input: a name as a string
# Result: a string
# task 2
def welcome_message(name:str) -> str:
   message = "Hello, " + name + "."

   return message


message = welcome_message("aunickel@calpoly.edu")
print(message)
#task 3
def smallest(n: float, m: float) -> float:
   if n < m:
      return n  # For which calls below is this statement evaluated?
   else:
      return m


first = smallest(3, 2)  # What is the value of first? first: 2
second = smallest(2, 2)  # What is the value of second? Is this a reasonable result? Why or why not? second: 2
print()


def function2(a: int, b: int, c: int) -> int:
   if a > b and a > c:
      return a - b  # In general, when will a call to this function evaluate this statement? when a is bigger than b and c
   elif b > c:
      return b + c  # In general, when will a call to this function evaluate this statement? if a isnt bigger than b or c
   else:
      return 2 * c  # In general, when will a call to this function evaluate this statement? if a is something else than bigger than b or c


answer1 = function2(3, 2, 1)  # What is the value of answer1? answer = 1
answer2 = function2(2, 3, 1)  # What is the value of answer2? answer 2: 4
answer3 = function2(2, 1, 3)  # What is the value of answer3? anser 3: 6
print()
#task 4

def checked_access(L: list[int], idx: int) -> Optional[int]:
   test = idx >= 0 and idx < len(L)  # What is the value of test on each call? 2, and 9
   if test:  # What is this check preventing? Checked access doesn't exceed len(L)
      return L[idx]
   else:
      return None


first = checked_access([1, 0, 1], 9)  # What is the value of first? false
second = checked_access([1, 0, 1], 2)  # What is the value of second? true
print()


def length_sum(L: list[str]) -> int:
   if len(L) > 2:
      result = len(L[0]) + len(L[1]) + len(L[2])  # For which call below is this statement evaluated= the first one
   elif len(L) > 1:  # and what are the values being added?
      result = len(L[0]) + len(L[1])  # For which call below is this statement evaluated 3rd one
   elif len(L) > 0:  # and what are the values being added?
      result = len(L[0])  # For which call below is this statement evaluated= 2nd one
   else:  # and what are the values being added?
      result = 0
   return result


first = length_sum(["this", "is", "the", "first", "call"]) #this equals 9
second = length_sum(["second call"]) #this equals 11
third = length_sum(["another", "call"]) #this equals 11
print()


def surprising(L: list[str], other: str) -> list[str]:
   L.append(other.upper())
   return L


words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
# What is the value of words at this point? this is confusing code
# What are the values of first and second at this point? this is confusing code, avoid such
# What happened? first and 2nd equals each other 
print()