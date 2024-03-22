def output_text_to_console(text):
    """
    Outputs the text to the console

    Parameters:
        text (str): text that is needed to be written in the console
    """
    print(text)


def write_to_file_builtin(file_path, content):
    """
    Writes to the file

    Parameters:
        file_path (str): Path to the file that we want write something to
        content (str): The content that needs to be written in the file
    """
    with open(file_path, 'a') as file:
        file.write(content)
