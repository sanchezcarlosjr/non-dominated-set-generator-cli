from src.app import main, __version__
from unittest.mock import Mock

# To test the entire project and print output, run this from the root directory:
# python -m pytest -s

# To test a specific function...
# python -m pytest -s tests/test_app.py
def test_should_asserts_same_version():

    # This is how we can 'fake' the input/functionality of dependant modules.

    # Mock the arguments.
    mock_args = Mock()
    mock_args.version = True

    # Mock the parser.
    mock_parser = Mock()
    mock_parser.add_argument = Mock()
    mock_parser.parse_args = Mock(return_value=mock_args)

    # If we call main() with a version argument, it should be returned.
    returned_version = main(mock_parser)
    assert __version__ == returned_version

def test_should_asserts_making_file():
    mock_args = Mock()
    mock_args.file = "1" 
    
    mock_parser = Mock()
    mock_parser.add_argument = Mock()
    mock_parser.parse_args = Mock(return_value=mock_args)
    
    main(mock_parser)

