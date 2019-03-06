import unittest
from Project import Project
from test_project import TestProject
def main():
    """Runs the unit tests"""

    suite = unittest.TestSuite()

    suite.addTests(unittest.makeSuite(TestProject))

    result = unittest.TextTestRunner(verbosity=1).run(suite)

    n_errors = len(result.errors)
    n_failures = len(result.failures)

    if n_errors or n_failures:
        print('\n\nSummary: %d errors and %d failures reported\n'
            (n_errors, n_failures))

    print()

main()