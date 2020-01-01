for i in range (10001):
    pass
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                s=pow(a,4)+pow(b,4)+pow(c,4)+pow(d,4)
                if i==s:
                    print(s)
                else:
                    print("Not Equal")