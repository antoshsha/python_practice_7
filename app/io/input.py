def input_text_from_console():
    """
    Inputs the text from console
    """
    return input("write some text: ")


def read_from_file_builtin(file_path):
    """
    Reads from the file using the built-in options

    Parameters:
        file_path (str): Path to the file to read from
    """
    with open(file_path, 'r') as file:
        return file.read()


def read_from_file_pandas(file_path):
    """
    Reads from the file using pandas

    Parameters:
        file_path (str): Path to the file to read from
    """
    import pandas as pd
    return pd.read_csv(file_path).to_string(index=False)
