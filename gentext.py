"""Create multiple text files."""
import os

# replacement strings
WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\n'


def create_text_files(_path, _file_prefix, _file_suffix, _num):
    """Create multiple text files with unix line ending.

    https://stackoverflow.com/questions/36422107/how-to-convert-crlf-to-lf-on-a-windows-machine-in-python/43678795#43678795#43678795

    Args:
        _path (string): path to file
        _file_prefix (string): filename
        _file_suffix (string): file suffix
        _num (integer): number of files
    """
    try:
        isdir = os.path.isdir(_path)
        if isdir is False:
            os.mkdir(_path)
    except OSError as error:
        print(error)

    for i in range(_num):
        content = f'cd /to/some/path \n./some_command --some_param {i}'

        file_path = f'{_path}/{_file_prefix}{i:03d}{_file_suffix}'
        print(file_path)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

        with open(file_path, 'rb') as open_file:
            content = open_file.read()

        # Convert line endings
        # Windows ➡ Unix
        content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)

        # Unix ➡ Windows
        # content = content.replace(UNIX_LINE_ENDING, WINDOWS_LINE_ENDING)

        with open(file_path, 'wb') as open_file:
            open_file.write(content)


if __name__ == '__main__':
    PATH = 'output'
    FILE_PREFIX = 'flow'
    FILE_SUFFIX = '.sh'
    NUM = 12
    create_text_files(PATH, FILE_PREFIX, FILE_SUFFIX, NUM)
