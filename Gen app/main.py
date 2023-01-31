print("Welcome to this Generation Identifier app")
print()

birthYear = int(input("Which year were you born?> "))
if birthYear >= 1888 and birthYear <= 1900:
  print("Hey! Tell me something the World War 1")
elif birthYear >= 1901 and birthYear <= 1927:
  print(
    "Greatest Generation, Must have been tought growing during the Great Depression"
  )
elif birthYear >= 1928 and birthYear <= 1945:
  print("Silent Generation")
elif birthYear >= 1946 and birthYear <= 1964:
  print("Baby Boomers")
elif birthYear >= 1965 and birthYear <= 1980:
  print("Hey, Generation X")
elif birthYear >= 1981 and birthYear <= 1996:
  print("aha! Millenials")
elif birthYear >= 1997 and birthYear <= 2012:
  print("Generation Z, TitTok is alot of fun right?")
elif birthYear >= 2012 and birthYear <= 2023:
  print("Hey Generation Alpha")
else:
  print("This year is not in the range of 1900-2023")
