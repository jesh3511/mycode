#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)
proto3=[1,2,3,4,5]#defining the list that will be used 
proto.insert(2,proto3)#inserts the new list into proto list
print(proto)#displays updated proto list
protoa.insert(len(protoa),proto3)#equal to append
print(protoa)#prints updated protoa list
