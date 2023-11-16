"""
更高的温度


"""

def more_higher(nums):

    res=[0]*len(nums)
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[j]>nums[i]:
                res[i]=j-i
                break

    return res

def window(nums):
    num=[nums[0]]
    res=[]
    for i in range(len(nums)):
        if




def main():
    example=[30,45,23,43,54,90]
    res=more_higher(example)
    print(res)

if __name__=='__main__':
    main()

