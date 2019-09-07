a,b,c,d = (int(z) for z in input().split())


item_total = a * 2

order_total = b + c + d

if order_total <= item_total:
    print("possible")
else:
    print("impossible")