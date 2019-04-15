import lee, brod

def todo(line):
    print('Not implemented.')


def translate(line):
    # get first word in line
    index = 0
    while line[index] == ' ':
        index += 1
    start = index
    while line[index] != ' ':
        index += 1
    firstword = line[start:index]
    # translate it to python 
    if firstword in keywords:
        return keywords[firstword](line)
    elif ':' in line:  # inside a case statement tell me if you think of a nicer way
        todo(line)
    elif '<-' in line:
        return operators(line)
    else:  # empty or not implemented
        return ''


def operators(line):  # deals with comparisons and assignments can be used by other functions
    for i in maths:
        line = line.replace(i, maths[i])
    return line


def comment(line):
    return '#' + line[2:]


def declaration(line):
    return '# ' + line


filename = input('Input CIEdocode file:')

file = open(filename + '.txt', 'r')
code = file.read().split('\n')
file.close()

indentNum = 0

maths = {'=': '==', '<-': '=', '^': '**', '<>': '!=',
         'OR': 'or', 'AND': 'and', 'NOT': 'not'}

other = {'//': comment, 'DECLARE': declaration}

selection = {'IF': todo, 'ELSE': todo, 'ENDIF': todo,
             'CASE': todo, 'OTHERWISE': todo, 'ENDCASE': todo
             }

loops = {'FOR': todo, 'ENDFOR': todo,
         'REPEAT': todo, 'UNTIL': todo,
         'WHILE': todo, 'ENDWHILE': todo
         }

keywords = {**other, **selection, **loops}

pyfile = open(filename + '.py', 'w')
for line in code:
    pythonline = translate(line)
    pyfile.write('\t' * indentNum + pythonline + '\n')

pyfile.close()
