# Author: Daniel E. Rodriguez Olivera
# Date: September 1, 2022
import ply.lex as lex

#reserved tokens/(taken)words for the ID token
reserved = { 'def' : 'DEF', 'var' : 'VAR', 'Int' : 'INT', 'if' : 'IF','else' : 'ELSE'}

# List of Tokens
tokens = ('ID', 'DEF', 'VAR', 'INT', 'IF', 'ELSE', 'NUM', 'LPAREN', 'RPAREN',
            'LBRACE', 'RBRACE', 'EQ', 'BECOMES', 'NE', 'LT', 'GT','LE',
            'GE', 'PLUS', 'MINUS', 'STAR', 'SLASH', 'PCT', 'COMMA', 'SEMI',
            'COLON', 'ARROW', 'COMMENT', 'WHITESPACE')

# Regular Expression rules for tokens

def t_ID(t): # RE for a string consisting of a letter (in the range a-z or A-Z) followed by zero or more letters and digits (in the range 0-9), but not equal to any of the keywords def, var, Int, if, else.
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

t_DEF = r'def' # RE for the string (keyword) def
t_VAR = r'var' # RE for the the string (keyword) var
t_INT = r'Int' # RE for the string (keyword) Int
t_IF = r'if' # RE for the the string (keyword) if
t_ELSE = r'else' # RE for the the string (keyword) else

def t_NUM(t): # RE for a string of one or more digits
    r'[0-9]+'
    t.value = int(t.value)
    return t
    
t_LPAREN = r'\(' # RE for the string (
t_RPAREN = r'\)' # RE for the string )
t_LBRACE = r'\{' # RE for the string {
t_RBRACE = r'\}' # RE for the string }
t_EQ = r'==' # RE for the string ==
t_BECOMES = r'=' # RE for the string =
t_NE = r'\!=' # RE for the string !=
t_LT = r'\<' # RE for the string <
t_GT = r'\>' # RE for the string >
t_LE = r'\<=' # RE for the string <=
t_GE = r'\>=' # RE for the string >=
t_PLUS = r'\+' # RE for the string +
t_MINUS = r'-' # RE for the string -
t_STAR = r'\*' # RE for the string *
t_SLASH = r'/' # RE for the string /
t_PCT = r'\%' # RE for the string %
t_COMMA = r',' # RE for the string ,
t_SEMI = r';' # RE for the string ;
t_COLON = r'\:' # RE for the string :
t_ARROW = r'=\>' # RE for the string =>
t_ignore_COMMENT = r'\#.*' # RE for the string // followed by any characters other than the newline character (ascii 10, \n )
t_ignore_WHITESPACE = r'[ \t]' # RE for one of the following characters: tab (ascii 9, \t ), newline (ascii 10, \n ), carriage return (ascii 13, \r ), space (ascii 32)

#Change input to check against tokens
input = """ def f(a:Int, b:Int):Int = { var c:Int;
def g(a:Int, b:(Int)=>Int):Int = { b(a)
}
def h(c:Int):Int = {
def g():Int = { c-b
}
g() }
c = a+b;
g(c,h) }"""

 # Track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Give the lexer some input
lexer.input(input)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)