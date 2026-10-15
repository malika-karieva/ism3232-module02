# debug_log.md
# Author: Malika Karieva

## Bug 1
Error type: KeyError
File + line: _"/Users/malika/ism3232/module05_functions/week8_buggy.py", line 12__
What the error means: KeyError means that the code to access the key that does not exist
What I told the duck: I told the duck that the code looks inside the current dictionary (rec) for the exact key named 'amount'. 
What I tried: When I tried to explain the loop to the duck, I realized that line 12 is searching for the key 'amount'. However, when Python tried to access that key in the actual data, it couldn't find it because of a typo in the word in line 4. 
How I fixed it: I fixed the typo in the word 'amount' in line 4.

## Bug 2
Error type: TypeError
File + line: ile "/Users/malika/ism3232/module05_functions/week8_buggy.py", line 24, in <module>
    print(is_over_limit(total))
          ~~~~~~~~~~~~~^^^^^^^
  File "/Users/malika/ism3232/module05_functions/week8_buggy.py", line 17, in is_over_limit
    return amount > '1000'
What the error means: It means I am asking Python to mathematically compare a number to text, which is an impossible operation.
How I fixed it: I changed '1000' to 1000.

## After Fixing Both Bugs
Final output: _malika@eduroam-226-82-36 module05_functions % /usr/local/bin/python3 /Users/malika/ism3232/module05_functions/week8_buggy.py
DEBUG: rec = {'id': 1, 'name': 'Taylor', 'amount': 1200}
DEBUG: rec = {'id': 2, 'name': 'Jordan', 'amount': 450}
DEBUG: rec = {'id': 3, 'name': 'Morgan', 'amount': 3500}
Total: $5150.00 across 3 records
True
Did pytest pass? Yes / No: Yes

## AI Literacy Reflection
Did I use AI? Yes / No: No
If yes -- exact prompt I used: 
What AI explained: ___
What I changed myself: I fixed the typo in the word 'amount' in line 4 to fix bug 1. I changed the string value '1000' to a number value 1000 to fix bug 2. 
Can I explain every fixed line? Yes / No: Yes
I fixed the first bug by checking why the key couldn't be found. I saw a typo in the word 'amount' on line 12. Once I fixed that spelling mistake, the first bug was resolved.
For the second bug, I changed a string into a number on line 16. The code was trying to compare a regular number to text inside quotes ('1000'), which made it crash. I removed the quotes to make it a number comparison, and that fixed the issue.

## What I learned
[2-3 sentences]
I learned what it actually means to 'tell the duck' to solve a problem out loud. I also learned how to look closely at error logs to figure out exactly what is causing a bug, like catching typos in keys or fixing a mismatch between numbers and text. 
