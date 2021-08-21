friends = ["Kevin","Karen","Jim","Jim","Raja"]
another_list = [1,2,3]
print(friends[-1])
print(friends[1:])
print(friends[1:3])
friends.extend(another_list)
print(friends)

friends.append("a")
print(friends)

friends.insert(1,"hi")
print(friends)

friends.remove("Raja")
print(friends)

friends.pop()
print(friends)
#friends.clear();
print(friends.index("Kevin"))

print(friends.count("Jim"))
another_list.sort()
print(another_list)
another_list.reverse()
print(another_list)

friends2 = friends.copy()
print(friends2)
