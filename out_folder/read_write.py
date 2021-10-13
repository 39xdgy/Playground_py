

f = open('../test_folder/test2.txt', "a")

f.write("testing3")

f.close()

a = ["a", "b", "c", "d"]

def count(inp):
    return "a" in inp
x = [x with filter(count, a) as out: x = out.count("a")]

print(x)