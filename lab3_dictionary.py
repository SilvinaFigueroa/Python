

def in_order(num_list):
     
    indexNext = 0 
    for index in num_list:
        if(num_list[indexNext] < num_list[indexNext - 1]):
            indexNext += 1
            return True    
        else:
            return False    



if __name__ == '__main__':
    # Test out-of-order example
    nums1 = [5, 6, 7, 8, 3]
    if in_order(nums1):
        print('In order')
    else:
        print('Not in order')
        
    # Test in-order example
    nums2 = [5, 6, 7, 8, 10]
    if in_order(nums2):
        print('In order')
    else:
        print('Not in order')


        