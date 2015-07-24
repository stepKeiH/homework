# coding: utf-8

def readNumber(line, index):
    number = 0
    divide = 10
    point = False
    while index < len(line) and (line[index].isdigit() or line[index] == '.'):
        if line[index] == '.':
            point = True
            index += 1
        elif point == False:
            number = number * 10 + int(line[index])
            index += 1
        else:
            number = number + int(line[index]) / divide
            divide *= 10
            index += 1
    token = {'type': 'NUMBER', 'number': number}
    return token, index

def readPlus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1

def readMinus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1

def readMulti(line, index):
    token = {'type': 'MULTI'}
    return token, index + 1

def readDivi(line, index):
    token = {'type': 'DIVI'}
    return token, index + 1

def tokenize(line):
    """
    Tokenize the input line and return a list of tokens
    """
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = readNumber(line, index)
        elif line[index] == '+':
            (token, index) = readPlus(line, index)
        elif line[index] == '-':
            (token, index) = readMinus(line, index)
        elif line[index] == '*':
            (token, index) = readMulti(line, index)
        elif line[index] == '/':
            (token, index) = readDivi(line, index)
        else:
            raise Exception('Invalid character found: ' + line[index])
        tokens.append(token)
    return tokens

def evaluate_multi_and_divi(tokens):
    if len(tokens) < 2:
        return tokens

    if len(tokens) == 2:
        raise Exception('Invalid syntax')

    index = 2
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 2]['type'] != 'NUMBER':
                raise Exception('Invalid syntax')
            elif tokens[index - 1]['type'] == 'MULTI':
                tokens[index] = {'type': 'NUMBER', 'number': tokens[index - 2]['number'] * tokens[index]['number']}
                del tokens[index - 1]
                del tokens[index - 2]
                index -= 1
            elif tokens[index - 1]['type'] == 'DIVI':
                if tokens[index]['number'] == 0 or tokens[index]['number'] == 0.0:
                    raise Exception('Can not be divided by 0')
                tokens[index] = {'type': 'NUMBER', 'number': tokens[index - 2]['number'] / tokens[index]['number']}
                del tokens[index - 1]
                del tokens[index - 2]
                index -= 1
            elif tokens[index - 1]['type'] == 'PLUS' or tokens[index - 1]['type'] == 'MINUS':
                index += 1
            else:
                raise Exception('Invalid syntax')
        index += 1
    if tokens[-1]['type'] != 'NUMBER':
        raise Exception('Invalid syntax')
    return tokens


def evaluate_plus_and_minus(tokens):
    """
    Evaluate the list of tokens and return a calculated result
    """
    answer = 0
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if index > 1 and tokens[index - 2]['type'] != 'NUMBER':
                raise Exception('Invalid syntax')
            elif tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                raise Exception('Invalid syntax')
        index += 1
    return answer

def evaluate(tokens):
    tokens = evaluate_multi_and_divi(tokens)  # 第1段階の評価
    answer = evaluate_plus_and_minus(tokens)  # 第2段階の評価
    return answer

def main(line):
    tokens = tokenize(line)
    answer = evaluate(tokens)
    return answer

if __name__ == "__main__":
    main(line)
