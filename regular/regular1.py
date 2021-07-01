import re
# result = re.findall(r'.', 'AV is largest Analytics community of India')  # "." Любой символ кроме строки \n
# print(result)

# result = re.findall(r'\w', 'AV is largest Analytics community of India')  # \w все буквы или цифры
# print(result)

result = re.findall(r'\w+', 'AV is largest Analytics community of India and India')
print(result)

result = re.findall(r'^\w+', 'AV is largest Analytics community of India')  # Первое слово
print(result)

result = re.findall(r'\w+$', 'AV is largest Analytics community of India')  # Последние слово
print(result)

result = re.findall(r'\w\w', 'AV is largest Analytics community of India')
print(result)

result = re.findall(r'\b\w.', 'AV is largest Analytics community of India')
print(result)






result = re.findall(r'@\w+', 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
print result

result = re.findall(r'@\w+.\w+', 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
print result

result = re.findall(r'@\w+.(\w+)', 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
print result

result = re.findall(r'\d{2}-\d{2}-\d{4}', 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
print result

result = re.findall(r'\d{2}-\d{2}-(\d{4})', 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
print result

result = re.findall(r'\w+', 'AV is largest Analytics community of India')
print result

result = re.findall(r'[aeiouAEIOU]\w+', 'AV is largest Analytics community of India')
print result

result = re.findall(r'\b[aeiouAEIOU]\w+', 'AV is largest Analytics community of India')
print result

result = re.findall(r'\b[^aeiouAEIOU]\w+', 'AV is largest Analytics community of India')
print result

result = re.findall(r'\b[^aeiouAEIOU ]\w+', 'AV is largest Analytics community of India')
print result