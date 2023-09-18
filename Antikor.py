def p(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            x1, y1 = queens[i]
            x2, y2 = queens[j]
            
            
            if x1 == x2 or y1 == y2:
                return False
            
            
            if abs(x1 - x2) == abs(y1 - y2):
                return False
    
    return True