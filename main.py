from app.io.input import read_from_file_builtin, read_from_file_pandas, input_text_from_console
from app.io.output import output_text_to_console, write_to_file_builtin


def main():
    text_input = input_text_from_console()
    write_to_file_builtin('output.txt', text_input)
    output_text_to_console(text_input)

    file_content = read_from_file_pandas('pandas_text.txt')
    print(file_content)
    write_to_file_builtin('output.txt', file_content)
    output_text_to_console(file_content)

    file_content2 = read_from_file_builtin('test.txt')
    write_to_file_builtin('output.txt', file_content2)
    output_text_to_console(file_content2)


if __name__ == "__main__":
    main()
