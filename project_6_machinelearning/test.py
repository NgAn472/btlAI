from numpy import load
data = load('./data/lang_id.npz')
lst = data.files
list_data = []
for item in lst:
    list_data.append(data[item])
    print(item)
    print(data[item])
    print(data[item].shape)
print(list_data[3][1])