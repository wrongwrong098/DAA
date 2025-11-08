def fract(weights,profits,capacity):

    steps = 0
    n = len(weights)

    #calculate profit weight ratio
    ratio = [p/w for p,w in zip(profits,weights)]
    steps += n

    #combine all data 
    items = list(zip(weights,profits,ratio))
    steps += n

    # sort by ratio 
    items.sort(key=lambda x: x[2],reverse=True)
    steps +=n


    #total profit 

    total_profit = 0 
    for p,w,r in items:
        steps+=1
        if capacity > w:
            capacity -=1
            total_profit = p
            steps +=2
        else :
            total_profit = r* capacity
            steps+=1
            break

    print('Maximum Profit -',total_profit)
    print("Steps count - ",steps)


weights = [10, 20, 30]
profits = [60, 100, 120]
capacity = 50

fract(weights,profits,capacity)
