"""
User Get Key Value Input Dictionary Start
"""

dic = {
    "google": "google is provide job and internship.",
    "amezon": "amezon is e-commerce store and cloud computing provider.",
    "zoom": "zoom is provide video call system to connecting meeating.",
    "microsoft": "microsoft is owner of windows and office software.."
}
# For beginner
print("google")
print("amezon")
print("zoom")
print("microsoft")
key = input("search detail of dectionary! \n")
print(dic[key.lower()])

# For advance
while True:
    for index, item in dic.items():
        print(index)
    key = input("search detail of dectionary! \n")
    print(dic[key.lower()])
    if int(input("Press 1 to exit 0 to continue \n")):
        break

"""
User Get Key Value Input Dictionary End
"""
