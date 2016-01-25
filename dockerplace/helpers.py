

def is_there_makefile(output=None):
    """
    get the output of a file listing
    and return True if there is a
    Makefile
    """
    if output is None:
        output = ""

    if "Makefile" in output:
        return True


def parse_make(content):
    """
    get the content of a makefile run and extract info from it
    """
    return content.split()


def sanitize(text):
    """
    get a string and clean it up from dangerous stuff
    """
    return text.split(";")[0]
