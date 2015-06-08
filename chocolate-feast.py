def chocolate(n,c,m):
    bars = n/c

    wrappers = bars

    while wrappers >=m:
        trade = wrappers/m
        bars += trade
        wrappers %= m
        wrappers += trade
        
    print bars

test_cases = int(raw_input().strip())
for _ in range(test_cases):
    A,B,C1 = [int(x) for x in raw_input().split()]
    chocolate(A,B,C1)
