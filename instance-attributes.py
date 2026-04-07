"""
- An instance attribute is a piece of information that belongs to a specific object created from a class.
- In our example, self.errors is an attribute of a particular form.
- Each form object has its own copy of errors.
- Methods (like validate()) can change these attributes.
- After running a method, you can look at the attribute to see the result.


Example:
  form = SimpleForm("ab", "123")
  form.validate()
  print(form.errors)  # Shows the errors for this particular form
"""

from typing import List, Optional

class SimpleForm:
    def __init__(self, username: str, password: str, errors: Optional[List[str]] = None):
        self.username = username
        self.password = password
        self.errors = errors  # can start as None

    def validate(self):
        if self.errors is None:
            self.errors = []

        if len(self.username) < 3:
            self.errors.append("Username too short")

        if len(self.password) < 6:
            self.errors.append("Password too short")

        return len(self.errors) == 0
    

form = SimpleForm("ab", "123")
if not form.validate():
    print(form.errors)  # Output: ['Username too short', 'Password too short']

"""
- self.errors is like a box attached to a specific form.
- .append("message") is like putting a note in the box.
- Every time something is wrong, you put a new note in the box.
- After checking everything, you can look inside the box to see all the problems.
"""



