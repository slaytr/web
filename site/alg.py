import collections
k = 5
seq = [1,2,3,4,5,6,7,8,9,1,3,2,4,2,1]
counts = collections.defaultdict(int)
for i in seq:
    if len(counts) < k:
        counts[i] += 1
    else:
        if i in counts:
            counts[i] += 1 
        else:
            end = False
            for j in counts:
                if counts[j] == 0:
                    del counts[j]
                    counts[i] += 1 
                    end = True
                    break
            if not end :
                for j in counts:
                    counts[j] -= 1
    print(counts)
                    
    
print(len(counts))
print(counts)

