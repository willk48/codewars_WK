def find_missing(sequence):
    curr = 0
    for item in sequence:
        diff = sequence[sequence.index(item)+1]-item
        if sequence.index(item)==0:
            curr = diff
        else:
            print(f'diff-{diff},recent_diff-{curr}')
            if diff != curr:
                if diff > curr:
                    return item + min([curr,diff])
                else:
                    return sequence[sequence.index(item)-1] + min([curr,diff])
