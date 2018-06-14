# compares 2 files and deletes the duplicates from the first (out2.txt)

with open("out2.txt", "r") as f1:
    file1 = f1.read().split()
with open("trims.txt", "r") as f2:
    file2 = f2.read().split()

res = set(file1).difference(set(file2))
result = "\n".join(res)
print(result)
with open("out2.txt", "w") as f1w:
    f1w.write(result)
