print('w1 w2 w3 w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                for w1 in range(0,2):
                    for w2 in range(0,2):
                        for w3 in range(0,2):
                            w1 = not(x and y) or z
                            w2 = not(x) or (y <= z)
                            w3 = not(x) or y or z
                            if (w and (w1 and w2 and w3) or (w1 and w2) or (w1 and w3) or (w2 and w3)):
                                print(w1, w2, w3,w)
