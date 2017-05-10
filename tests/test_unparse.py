from typed_ast import ast3 as ast
import sys
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

import astunparse
from tests.common import AstunparseCommonTestCase

class UnparseTestCase(AstunparseCommonTestCase, unittest.TestCase):

    def assertASTEqual(self, ast1, ast2):
        self.assertEqual(ast.dump(ast1), ast.dump(ast2))

    def check_roundtrip(self, code1, filename="internal", mode="exec"):
        ast1 = ast.parse(str(code1))
        code2 = astunparse.unparse(ast1)
        ast2 = ast.parse(code2)
        self.assertASTEqual(ast1, ast2)
