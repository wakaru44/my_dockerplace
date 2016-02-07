

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
