'''
2018/11/29

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

＃無理やりすぎるし美しくない…
＃ここから連携テスト
'''

def fiboNacci():
    fibos = []
    evenNum = []
    sumNum = 0
    full = 4000000

    for fbn in range(0,100):
        if fbn <= 2:
            fibos.append(fbn+1)
        elif (fibos[-1] >= full):
            break
        else:
            f1 = fbn - 1
            f2 = fbn - 2
            fibos.append (fibos[f1]+fibos[f2])
        
        numCheck = fibos[fbn] / 2
        if numCheck.is_integer() == True:
            evenNum.append(fibos[fbn])
    
    for i in range(len(evenNum)):
        sumNum += evenNum[i]
    
    print (sumNum)

fiboNacci()


