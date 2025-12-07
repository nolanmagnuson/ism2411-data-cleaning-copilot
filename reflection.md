## Reflection

### What Copilot Generated
I used GitHub Copilot to help me write two functions in my script:
`load_data()` and `clean_column_names()`. I started by typing the function
names and docstrings, and Copilot suggested code. For example, Copilot
generated a version of `clean_column_names()` that used a longer chain of
string operations, and I accepted the core idea but simplified it to make
the code easier for me to understand.

### What I Modified
I made several changes to the original Copilot suggestions. Copilot first
suggested filling missing values with 0, but I decided that didn't make
sense for sales data, so I changed the logic to drop rows with missing
prices or quantities. Copilot also suggested taking the absolute value of
negative numbers, which I removed because it would “fix” errors instead of
highlighting them. I also changed variable names and added comments to make
the code clearer and more appropriate for an intro-level project.

### What I Learned
I learned how important it is to clean data before analyzing it, because
messy data can lead to wrong results. I also learned how to use pandas to
standardize column names, convert numeric types, and remove invalid rows.
Using Copilot taught me that AI can be a helpful starting point, but it is
not always correct. I still needed to think about each suggestion and
decide whether it made sense for the dataset. This helped me understand the
difference between blindly accepting code and using Copilot responsibly as
a coding assistant.
