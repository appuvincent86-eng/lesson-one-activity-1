my_list=[12, 33, 56, 1111111111111111105, 90, 71]
print(my_list)
evencoolermy_list=[i for i in my_list if i%2==0]
print(evencoolermy_list)
coolermy_list=[i*2 for i in my_list]
print(coolermy_list)
# Output:
# [12, 33, 56, 1111111111111111105, 90, 71]
# [12, 56, 90]
# [24, 66, 112, 2222222222222222210, 180, 142]
# (.venv-1) PS C:\Users\HP\Desktop\good folder> 
