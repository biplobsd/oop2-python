d = dict()
for m in input():
    try:
        d[m] += 1
    except KeyError:
        d[m] = 1

d = sorted(d.items(), key=lambda item: item[1], reverse=True)

just3 = d[:3]

if len(set(v[1] for v in just3)) == 1:
    just3.sort(key=lambda x: x[0])

for mm in just3:
    print(mm[0], mm[1])
