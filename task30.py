online = input("Is online (True/False): ") == "True"
is_typing = input("Is typing (True/False): ") == "True"

result = online and not is_typing
print(result)