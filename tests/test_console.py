import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    @patch('sys.stdout', new=StringIO())
    def test_quit(self):
        with self.assertRaises(SystemExit):
            HBNBCommand().onecmd("quit")

    @patch('sys.stdout', new=StringIO())
    def test_help(self):
        HBNBCommand().onecmd("help")
        output = sys.stdout.getvalue().strip()
        self.assertIn("Documented commands (type help <topic>):", output)

    @patch('sys.stdout', new=StringIO())
    def test_create_missing_class(self):
        HBNBCommand().onecmd("create")
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    @patch('sys.stdout', new=StringIO())
    def test_create_invalid_class(self):
        HBNBCommand().onecmd("create InvalidClass")
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    @patch('sys.stdout', new=StringIO())
    def test_create_valid_class(self):
        HBNBCommand().onecmd("create BaseModel")
        output = sys.stdout.getvalue().strip()
        self.assertRegex(output, r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")

    @patch('sys.stdout', new=StringIO())
    def test_show_missing_class(self):
        HBNBCommand().onecmd("show")
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    @patch('sys.stdout', new=StringIO())
    def test_show_invalid_class(self):
        HBNBCommand().onecmd("show InvalidClass")
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    @patch('sys.stdout', new=StringIO())
    def test_show_missing_id(self):
        HBNBCommand().onecmd("show BaseModel")
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    @patch('sys.stdout', new=StringIO())
    def test_show_valid_instance(self):
        HBNBCommand().onecmd("create BaseModel")
        output = sys.stdout.getvalue().strip()
        instance_id = output

        sys.stdout = StringIO()
        HBNBCommand().onecmd(f"show BaseModel {instance_id}")
        output = sys.stdout.getvalue().strip()
        self.assertIn(instance_id, output)

    # Add more tests for other commands...


if __name__ == '__main__':
    unittest.main()

