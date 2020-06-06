inputs = [int(i) for i in input().split(" ")]
inputs=sorted(inputs)
aplusbplusc= inputs[-1]
aplusb=inputs[0]
bplusc=inputs[1]
aplusc = inputs[2]
print(aplusbplusc-bplusc,aplusbplusc-aplusc,aplusbplusc-aplusb)
