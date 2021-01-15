stockprice = [80,100,110,90,65,70,75,70,65,60,55,50]
A = []

for i in range(1,len(stockprice)):
    A.append(stockprice[i]-stockprice[i-1])
print(A)
    
def maxsumofarr(A,left,mid,right):
    sum1=0
    left_sum=-10000
    left_max=mid
    for i in range(mid,left-1,-1):
        sum1+=A[i]
        if(sum1>left_sum):
            left_sum=sum1
            left_max=i
    sum2=0
    right_sum=-1000
    right_max=mid+1
    for i in range(mid+1,right+1):
        sum2+=A[i]
        if(sum2>right_sum):
            right_sum=sum2
            right_max=i
    return left_sum+right_sum,left_max+1,right_max+1


def maxsubarrsum(A,left,right):
    if(left==right):
        return A[left],left+1,right+1
    mid=int((left+right)/2)
    return max(maxsubarrsum(A,left,mid),maxsubarrsum(A,mid+1,right),maxsumofarr(A,left,mid,right))


right=len(A)-1
max_sum=maxsubarrsum(A,0,right)
print(max_sum)