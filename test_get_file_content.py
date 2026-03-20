from functions.get_file_content import get_file_content

result_lorem = get_file_content("calculator", "lorem.txt")
print(f"Lorem length: {len(result_lorem)}")
print(result_lorem[-100:])  # print the end to check for truncation message

result = get_file_content("calculator", "main.py")

print("Result for current directory:")
print(result)

result1 = get_file_content("calculator", "pkg/calculator.py")
print("Result for 'pkg' direcotry")
print(result1)

result2 = get_file_content("calculator", "/bin/cat")
print("Result for '/bin' directory")
print(result2)

resutl3 = get_file_content("calculator", "pkg/does_not_exist.py")
print("Result for '../' directory")
print(resutl3)