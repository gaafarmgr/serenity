import ply.lex as lex

# Disabling the invalid-name option because the naming style of the various
# token regex constants below are mandated by lex and shouldn't be flag.
# Disabling unused-argument because it's triggering for tokenizer methods that
# require a parameter be present, even if it isn't used.
# pylint: disable=invalid-name,unused-argument

# Token names
tokens = [
   'NUMBER',
   'NAME',
   'TYPE',
   'STRING',
   'COMMENT',
   'BCOMMENT',
   'LBRACE',
   'RBRACE',
   'LPAREN',
   'RPAREN',
   'LBRACKET',
   'RBRACKET',
   'SEMICOLON',
]

# Define specific label keywords
keywords = {
    'struct':  'STRUCT',
    'include': 'INCLUDE',
    'typedef': 'TYPEDEF',
    'if':      'IF',
    'else':    'ELSE',
}
tokens += keywords.values()

# When we find a number, convert it from a string to a number
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# When we find a number, convert it from a string to a number
def t_CHAR(t):
    r'\'([^\\\n]|(\\.))*?\''
    t.value = int(t.value)
    return t

def is_type(t):
    """ Placeholder function until typesystem is implemented. """
    if t == "int":
        return True

    return False

def t_NAME(t):
    r'[a-zA-Z][a-zA-Z0-9_\.-]*'
    if t.value in keywords:
        t.type = keywords[t.value]
    #if is_type(t.value):
    #    t.type = "TYPE"
    return t

def t_COMMENT(t):
    r'//.*'
    pass

def t_BCOMMENT(t):
    r'/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/'
    pass

# Some regex rules for simple tokens
t_STRING    = r'\"([^\\\n]|(\\.))*?\"'
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACKET  = r'\['
t_RBRACKET  = r'\]'
t_SEMICOLON = r'\;'

# This is so we cn keep track of line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

def get_location(t):
    last_cr = t.lexer.lexdata.rfind("\n", 0, t.lexpos)
    if last_cr < 0:
        last_cr = 0
    column = (t.lexpos - last_cr)
    return (t.lexer.lineno, column)

# Error handling rule
def t_error(t):
    line, col = get_location(t)
    print("Illegal character '{}' at [line:{}, col:{}]".format(
            t.value[0], line, col))
    t.lexer.skip(1) # TODO: break parsing here

def create_lexer():
    return lex.lex()
