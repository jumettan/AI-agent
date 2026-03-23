from functions.run_python_file import run_python_file

result = run_python_file("calculator", "main.py")

print("Result for current directory:")
print(result)

result1 = run_python_file("calculator", "main.py", ["3 + 5"])
print("Result for 'pkg' direcotry")
print(result1)

result2 = run_python_file("calculator", "tests.py")
print("Result for '/bin' directory")
print(result2)

result3 = run_python_file("calculator", "../main.py")
print("Result for '../' directory")
print(result3)

result4 = run_python_file("calculator", "nonexistent.py")
print(result4)

result5 = run_python_file("calculator", "lorem.txt")
print(result5)