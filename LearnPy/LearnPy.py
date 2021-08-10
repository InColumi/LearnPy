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

def calculate(numbers: list):
    sizePerson = 3
    sum = getSum(numbers)
    max, min = getMaxMin(numbers)
    matrix = [['#' for j in range(sum)] for i in range(max + min + sizePerson)]
    PringMatrix(matrix)

def main():
    numbers = [1,2,3,4,5]
    #numbers = [2,15,18,5,16,17,10,1,19,2,1,16,14,1,16,2,5,13,11,10]
    #userInput = input().split(' ')
    #for i in userInput:
    #    numbers.append(int(i))
    #numbers = input().split(' ')
    calculate(numbers)

if __name__ == "__main__":
    main()