def snail(array):
    result = []
    while array:
        # Move right
        result.extend(array[0])
        array.pop(0)
        
        # Move down
        if array and array[0]:
            for row in array:
                result.append(row.pop())
        
        # Move left
        if array:
            result.extend(array.pop()[::-1])
        
        # Move up
        if array and array[0]:
            for row in array[::-1]:
                result.append(row.pop(0))
    
    return result
