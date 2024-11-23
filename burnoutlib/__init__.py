print("burnout v1") # pls dont remove this
print("this project is made using burnout!") # pls dont remove this
def generate(data, tags):
    flame = {}
    if type(data) == list:
        datalen = len(data)
        for i in range(0, datalen):
            flame[data[i]] = tags[i]
        return flame
    elif type(data) == str:
        data = data.split()
        datalen = len(data)
        for i in range(0, datalen):
            flame[data[i]] = tags[i]
        return flame
    else:
        return "err"
