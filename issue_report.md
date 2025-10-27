
---



>  This file documents every issue found and the corresponding fixes you made.

```markdown
#  ISSUE REPORT – Static Code Analysis

| **No.** | **Tool Used** | **Type of Issue** | **Description** | **Line No.** | **Fix Applied / Action Taken** |
|----------|----------------|------------------|------------------|---------------|--------------------------------|
| 1 | Pylint | Variable Naming | Non-standard variable name `t` / `f` | Multiple | Renamed to more descriptive names |
| 2 | Pylint | Function Arguments | Mutable default argument `logs=[]` used in `addItem()` | Line 9 | Changed to `logs=None` and initialized inside function |
| 3 | Pylint | Exception Handling | Bare `except:` used in `removeItem()` | Line 20 | Replaced with `except KeyError:` to catch specific error |
| 4 | Pylint | Dangerous Function | Use of `eval()` is insecure | Line 58 | Removed `eval()` call |
| 5 | Bandit | Insecure File Handling | Files opened without context managers | Multiple | Changed to `with open(...) as f:` syntax |
| 6 | Bandit | Type Checking Missing | User inputs not validated | Multiple | Added `isinstance()` checks for type safety |
| 7 | Flake8 | Formatting | Missing blank lines and inconsistent indentation | Throughout | Formatted code using `black` |
| 8 | Logic | Incorrect Quantity Update | Negative qty allowed for `addItem("banana", -2)` | Line 48 | Added validation to prevent negative quantities |

---

**Result:**  
All critical issues were resolved in the final version `fixed_inventory_system.py`.  
The program now follows **PEP8**, **secure coding practices**, and is **functionally correct**.
