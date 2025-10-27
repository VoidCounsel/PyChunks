def greet(name):  # 'name' = param placeholder, empty till call
    print(f"Inside func: name is already '{name}' (type: {type(name)})")  # Bound! No undeclared error.
    name = type_test(name, str, 'name')  # Validates the existing 'name', reassigns if good (or raises)
    print(f"After check: name is still '{name}'")
    return f"Hi {name}"

# Your mantra helper (from before, chaining edition)
def type_test(value, expected_type, param_name="value"):
    if not isinstance(value, expected_type):
        raise TypeError(f"{param_name}: expected {expected_type.__name__}, got {type(value).__name__} ({repr(value)})")
    return value  # Returns it for chaining/reassign

# Call time: The magic moment
greet("Bob")  # Passes str—outputs: Inside func: name is already 'Bob' (type: <class 'str'>)
              # After check: name is still 'Bob'
              # Hi Bob

# Or chain fresh: greet(type_test(input('Name? '), str, 'name'))  # Validates input on-the-fly, no juggling
