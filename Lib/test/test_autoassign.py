"Test the functionality of auto-assignment of attributes."

import unittest

class ClassTests(unittest.TestCase):
    def test_assign_regular_argument(self):
        class Klass:
            def __init__(self, @value):
                pass

        my_object = Klass(2)
        self.assertEqual(my_object.value, 2)

    def test_dont_assign_regular_argument_without_autoassign(self):
        class Klass:
            def __init__(self, @value, another_value):
                pass

        my_object = Klass(2, 5)
        self.assertEqual(my_object.value, 2)
        self.assertRaises(AttributeError, getattr, my_object, "another_value")

    def test_assign_multiple_regular_arguments(self):
        class Klass:
            def __init__(self, @value, @another_value):
                pass

        my_object = Klass(2, "fifty")
        self.assertEqual(my_object.value, 2)
        self.assertEqual(my_object.another_value, "fifty")

    def test_assign_posonly_argument(self):
        class Klass:
            def __init__(self, @value, /):
                pass

        my_object = Klass(2)
        self.assertEqual(my_object.value, 2)

    def test_assign_kwonly_argument(self):
        class Klass:
            def __init__(self, *, @value=20):
                pass

        my_object = Klass(value=20)
        self.assertEqual(my_object.value, 20)

    def test_assign_regular_kwonly_argument(self):

        class Klass:
            def __init__(self, a, @b, /, c, @d, @e=1, *, f=2, @g=3):
                pass

        my_object = Klass(1, 2, 3, 4, e=5, f=6)
        self.assertEqual(my_object.b, 2)
        self.assertEqual(my_object.d, 4)
        self.assertEqual(my_object.e, 5)
        self.assertEqual(my_object.g, 3)
        self.assertRaises(AttributeError, getattr, my_object, "a")
        self.assertRaises(AttributeError, getattr, my_object, "c")
        self.assertRaises(AttributeError, getattr, my_object, "f")


if __name__ == '__main__':
    unittest.main()
