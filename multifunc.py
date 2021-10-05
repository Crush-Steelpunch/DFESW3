def add_two_to_two_numbers(num1In,num2In):
    out1Var = num1In + 2
    out2Var = num2In + 2
    outList = [ out1Var,out2Var]
    return outList

inputNum1 = int(input('num1: '))
inputNum2 = int(input('num2: '))
outNum = add_two_to_two_numbers(inputNum1,inputNum2)

print(outNum)