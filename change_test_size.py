ts = open("TestSize.txt", "r")
ts =  float(ts.read())

new_ts = open("TestSize.txt", "w")
newts = ts - 0.05
new_ts.write(str(newts))
new_ts.close()
