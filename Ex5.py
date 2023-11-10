def print_comb():
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if (i < j < k):
                    print(i, j, k)

print_comb()