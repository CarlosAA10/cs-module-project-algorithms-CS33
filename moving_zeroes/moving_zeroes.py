'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here

    swaps = True

    while swaps:

        swaps = False 

        for i in range(len(arr) - 1):

            if arr[i] is 0 and arr[i + 1] is not 0:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps = True
            
    

    
    # for i in range(len(arr) - 1):

    #     swaps = True

    #     while swaps:
    #         swaps = False

    #         if arr[i] is 0 and arr[i + 1] is not 0:
    #             arr[i], arr[i + 1] = arr[i + 1], arr[i]
    #             swaps = True
        
    
    return arr

arr = [0,1,0]

print(moving_zeroes(arr))


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")