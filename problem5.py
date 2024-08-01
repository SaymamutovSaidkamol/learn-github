def Encoded_list(num1):
    nums1  =[]
    index = 0
    for i in range(1,len(num1)+1):
        if i % 2:
            for j in range(num1[index]):
                nums1.append(num1[index+1])
            
        index += 1
    return nums1

# 1 chi e
print("1 chi example")
nums1 = [1,2,3,4]
print(nums1)
result1 = Encoded_list(nums1)
print(result1)

print("\n2 chi example")

# 2 chi example 
nums2 = [1,1,2,3]
print(nums2)
result2 = Encoded_list(nums2)
print(result2)

