def fibbo(n):
    steps=0
    if n <= 0 :
        print('Invalid Input!!')
        return
    elif n ==1:
        print(0)
        steps+=1
    else:
        a,b=0,1
        print(a,b,end=' ')
        steps+=2
        for i in range(2,n):
            c= a+b
            a,b=b,c
            print(c,end=' ')
            steps+=3
            

    print('The count of steps is - ',steps)

def fibbo_recursive(n,steps=[0]):
    steps[0] +=1
    if n <=1:
        return n;
    else:
        return fibbo_recursive(n-1,steps)+fibbo_recursive(n-2,steps)

n = int(input('Enter the No of terms u need - '))

print("\nIterative Fibonacci Series:")
fibbo(n)

print("\n Recursive Fibonacci Series:")
steps=[0]

for i in range(n):
    print(fibbo_recursive(i,steps),end=' ')
print('Steps Count Recursive - ', steps[0])