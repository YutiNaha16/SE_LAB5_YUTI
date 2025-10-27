Reflection – Static Code Analysis Lab

Which issues were the easiest to fix, and which were the hardest? Why?

The easiest was fixing PEP8 style issues (spacing, variable naming).

The hardest was understanding and correcting the mutable default argument (logs=[]), as it caused hidden state-sharing bugs.

Did the static analysis tools report any false positives?

Yes, Bandit flagged some low-risk warnings (like using print()), which were not security-critical for this simple script.

How would you integrate static analysis tools into your actual development workflow?

I would run Pylint, Bandit, and Flake8 automatically via pre-commit hooks or GitHub Actions CI to maintain consistent quality and catch issues early.

What tangible improvements did you observe in code quality after fixes?

Improved readability, fewer warnings, safe file handling, better error management, and removal of insecure eval() calls — making the script more robust and secure.
