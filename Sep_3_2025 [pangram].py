import time
start_time = time.perf_counter()
'''
---Pangram---
Given a word or sentence and a string of lowercase letters, determine if the word or sentence uses all the letters from the given set at least once and no other letters.
    Ignore non-alphabetical characters in the word or sentence.
    Ignore letter casing in the word or sentence.
'''
def is_pangram(sentence, letters):
    new_sent = []
    #You can separate the characters in a string in Python by using the list() function, which converts the string into a list of its individual characters. For example, list("hello") will give you ['h', 'e', 'l', 'l', 'o']
    #dict.fromkeys() method creates a dictionary with keys from the list, automatically removing duplicates because dictionary keys are unique. The order is preserved where dictionaries maintain insertion order.
    found = False
    sentence = list(dict.fromkeys(sentence))
    new_let = list(x.lower() for x in letters) #could be simplified to [x.lower() for x in letters] or even done earlier when processing the input.
    for x in sentence:
        if not x == " " and x.isalpha(): #only checking of x.isalpha() would be snough here
                new_sent.append(x.lower())
            
    if set(new_let) == set(new_sent):
            found = True

    print(found)

is_pangram("hello", "helo") #should return True
is_pangram("hello", "hel") #should return False
is_pangram("hello", "helow") #should return False
is_pangram("hello world", "helowrd") #should return True
is_pangram("Hello World!", "helowrd") #should return True
is_pangram("Hello World!", "heliowrd") #should return False
is_pangram("freeCodeCamp", "frcdmp") #should return False
is_pangram("The quick brown fox jumps over the lazy dog.", "abcdefghijklmnopqrstuvwxyz") #should return True

'''
simplified: :/
def is_pangram(sentence, letters):
    sentence_letters = {c.lower() for c in sentence if c.isalpha()}
    required_letters = set(letters.lower())
    return sentence_letters == required_letters

'''

''' 
---dict.fromkeys()---
The `dict.fromkeys()` method in Python is a class method that creates a new dictionary with keys from a given iterable (like a list or string) and assigns a specified value to each key. If no value is provided, it defaults to `None`. Its a quick way to initialize a dictionary when you want multiple keys to share the same starting value.

### Syntax:
```python
dict.fromkeys(iterable, value=None)
```
- `iterable`: An iterable (e.g., list, tuple, string) whose elements become the dictionary's keys.
- `value`: The value to assign to each key (optional; defaults to `None`).

### Common Use Cases:
1. **Initializing a Dictionary with Default Values**:
   When you need a dictionary with a set of keys, all starting with the same value (e.g., `0`, `[]`, or `None`).
   ```python
   keys = ['a', 'b', 'c']
   my_dict = dict.fromkeys(keys, 0)
   print(my_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}
   ```

2. **Creating a Dictionary from Unique Characters**:
   If you have a string and want to create a dictionary with its characters as keys, `dict.fromkeys()` automatically removes duplicates (since dictionary keys are unique).
   ```python
   chars = "hello"
   my_dict = dict.fromkeys(chars)
   print(my_dict)  # Output: {'h': None, 'e': None, 'l': None, 'o': None}
   ```

3. **Setting Up a Counter or Tracker**:
   Useful for initializing a dictionary to track occurrences or states, like in your pangram solution where you used it to deduplicate characters (though `set` was simpler).
   ```python
   items = ['apple', 'banana', 'apple']
   count_dict = dict.fromkeys(items, 0)
   for item in items:
       count_dict[item] += 1
   print(count_dict)  # Output: {'apple': 2, 'banana': 1}
   ```

4. **Quickly Creating a Lookup Table**:
   When you need a dictionary to map keys to a default value for quick lookups.
   ```python
   categories = ['low', 'medium', 'high']
   priority_map = dict.fromkeys(categories, 'Not Assigned')
   print(priority_map)  # Output: {'low': 'Not Assigned', 'medium': 'Not Assigned', 'high': 'Not Assigned'}
   ```

### Why You Used It:
In your pangram code, you used `dict.fromkeys(sentence)` to remove duplicate characters from the sentence by converting it into a dictionary’s keys. Since dictionary keys are unique, this effectively gave you a deduplicated list of characters when you converted it back to a list. However, as noted in the review, using `set(sentence)` directly would have been simpler because sets are designed specifically for unique elements and are more straightforward for this purpose.

### Gotchas:
1. **Mutable Default Values**: If you use a mutable object (like a list) as the `value`, all keys share the same object, which can lead to unexpected behavior.
   ```python
   my_dict = dict.fromkeys(['a', 'b', 'c'], [])
   my_dict['a'].append(1)
   print(my_dict)  # Output: {'a': [1], 'b': [1], 'c': [1]}  # All keys share the same list!
   ```
   To avoid this, use immutable values or create separate objects (e.g., with a dictionary comprehension).

2. **Order Preservation**: Since Python 3.7+, dictionaries preserve insertion order, so `dict.fromkeys()` maintains the order of the iterable’s elements.

3. **Performance**: `dict.fromkeys()` is slightly faster than a dictionary comprehension for initializing a dictionary with many keys, but for small inputs, the difference is negligible.

### When to Use It:
- Use `dict.fromkeys()` when you need a quick way to initialize a dictionary with a fixed set of keys and a common default value.
- Avoid it if you just need a collection of unique elements (use `set()` instead) or if you need complex logic for key-value pairs (use a dictionary comprehension).
'''
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.6f} seconds")