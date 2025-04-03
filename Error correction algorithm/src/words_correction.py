def correct_word(word, matrix):
    if len(word) != len(matrix[0,:]):
        return "BRAK"
    else:
        length = len(word)
        distances = [length]
        correct_word = None
        for i in range(length):
            d = length
            for j in range(length):
                if matrix[i,j] == word[j]:
                    d-=1
            if d < distances[0]:
                distances = [d]
                correct_word = matrix[i,:]
            elif d == distances[0]:
                distances.append(d)
        if len(distances) != 1 or distances[0] == length:
            return "BRAK"
        else:
            return correct_word