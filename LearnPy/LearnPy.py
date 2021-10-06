def PringMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end='')
        print()

def getMaxMin(numbers: list):
    sum = 0
    max = sum
    min = sum
    for i in range(len(numbers)):
        sum += numbers[i] if i % 2 == 0 else -numbers[i]
        if max < sum:
            max = sum
        if min > sum:
            min = sum
    return [max,abs(min)]

def getSum(numbers: list):
    sum = 0
    for i in numbers:
        sum += i
    return sum

def addPerson(matrix, i, j):
     matrix[i - 1][j] = 'o'
     matrix[i][j] = '|'
     matrix[i][j - 1] = '/'
     matrix[i][j + 1] = '\\'
     matrix[i + 1][j - 1] = '<'
     matrix[i + 1][j] = ' '
     matrix[i + 1][j + 1] = '>'

def calculate(numbers: list):
    sizePerson = 3
    sum = getSum(numbers)
    max, min = getMaxMin(numbers)
    matrix = [['#' for j in range(sum)] for i in range(max + min + sizePerson)]

    isUp = True
    i = len(matrix) - min - 1
    j = 0
    iStartPersone = 0
    jStartPersone = 0
    for k in range(len(numbers)):
        if k % 2 == 0:
            for p in range(numbers[k] - 1):
                matrix[i][j] = '/'
                i -= 1
                j += 1
            matrix[i][j] = '/'
        else:
            for p in range(numbers[k] - 1):
                matrix[i][j] = '\\'
                i += 1
                j += 1
            matrix[i][j] = '\\'
        j += 1
        if i == sizePerson:
            j += 1
            iStartPersone = i - 1
            jStartPersone = j - 1
    PringMatrix(matrix)

    matrix[iStartPersone - 1][jStartPersone] = 'o'
    matrix[iStartPersone][jStartPersone] = '|'
    matrix[iStartPersone][jStartPersone - 1] = '/'
    matrix[iStartPersone][jStartPersone + 1] = '\\'
    matrix[iStartPersone + 1][jStartPersone - 1] = '<'
    matrix[iStartPersone + 1][jStartPersone] = ' '
    matrix[iStartPersone + 1][jStartPersone + 1] = '>'

    PringMatrix(matrix)

def main():
    numbers = [2,15,18,5,16,17,10,1,19,2,1,16,14,1,16,2,5,13,11,10]
    userInput = input().split(' ')
    for i in userInput:
        numbers.append(int(i))
    numbers = input().split(' ')
    calculate(numbers)

if __name__ == "__main__":
    main()