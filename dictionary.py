monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March"
}

print(monthConversions["Jan"])
print(monthConversions["Mar"])
print(monthConversions.get("Jan"))
print(monthConversions.get("DDD","Not a valid key"))


