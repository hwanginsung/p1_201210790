def sumOfMultiple3_5(begin,end):
    sum=0
    for i in range(begin,end):
        if (i%3==0 or i%5==0):
            sum=sum+i
    print sum
    return sum