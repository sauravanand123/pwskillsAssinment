# file_operations.py

def read_file(file_path):
    """Read the content of a file and return it as a string."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: The file at {file_path} was not found."
    except Exception as e:
        return f"Error: {e}"

def write_file(file_path, data):
    """Write the given data to a file. Overwrite if the file already exists."""
    try:
        with open(file_path, 'w') as file:
            file.write(data)
        return f"Data successfully written to {file_path}"
    except Exception as e:
        return f"Error: {e}"

def append_to_file(file_path, data):
    """Append the given data to a file. Create the file if it does not exist."""
    try:
        with open(file_path, 'a') as file:
            file.write(data)
        return f"Data successfully appended to {file_path}"
    except Exception as e:
        return f"Error: {e}"
