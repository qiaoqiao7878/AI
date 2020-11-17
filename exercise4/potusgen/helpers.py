"""
@author: Lukas Schöbel 2019.
"""

import re

def cleanup_result(s):
    """Cleans a given string and fixes punctuation and capitalization

    :param s: 

    """

    # Whitespace & Padding correction
    s = re.sub('\\s+([.,!?])\\s*', r'\1 ', s)
    s = re.sub(r' ([\,\.\/\-\"\?\!\:\;])', "\\1", s)
    s = re.sub(r'( [a-zA-Z]) . ([a-zA-Z]) .', "\\1.\\2.", s)

    # Capitalization correction
    s = s.capitalize()
    s = re.sub(" i[,;!]? ", " I ", s)
    s = re.sub('([.!?]\\s+[a-z])', lambda c: c.group(1).upper(), s)
    
    return s