# import python library
import unittest

# import files
from TestHttpbin import TestHttpbin

suite = unittest.TestLoader().loadTestsFromTestCase(TestHttpbin)
unittest.TextTestRunner(verbosity=2).run(suite)
