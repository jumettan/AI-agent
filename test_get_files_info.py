from functions.get_files_info import get_files_info

result = get_files_info("calculator", ".")

print("Result for current directory:")
print(result)

result1 = get_files_info("calculator", "pkg")
print("Result for 'pkg' direcotry")
print(result1)

result2 = get_files_info("calculator", "/bin")
print("Result for '/bin' directory")
print(result2)

resutl3 = get_files_info("calculator", "pkg")
print("Result for '../' directory")
print(resutl3)