#You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. 
#You are allowed to swap any two elements. Find the minimum number of swaps required to sort the array in ascending order.

# Return the minimum number
# of swaps required to sort
# the array
def minSwap(arr, n):
     
    ans = 0
    temp = arr.copy()
 
    # Dictionary which stores the
      # indexes of the input array
    h = {}
 
    temp.sort()
 
    for i in range(n):
         
        #h.[arr[i]
        h[arr[i]] = i
         
    init = 0
     
    for i in range(n):
 
        # This is checking whether
        # the current element is
        # at the right place or not
        if (arr[i] != temp[i]):
            ans += 1
            init = arr[i]
 
            # If not, swap this element
              # with the index of the
              # element which should come here
            arr[i], arr[h[temp[i]]] = arr[h[temp[i]]], arr[i]
 
            # Update the indexes in
              # the hashmap accordingly
            h[init] = h[temp[i]]
            h[temp[i]] = i
             
    return ans
